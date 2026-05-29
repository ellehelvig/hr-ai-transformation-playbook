# Attrition risk modeling

This notebook builds a baseline attrition risk model on synthetic HR data. It demonstrates the model design, calibration analysis, fairness audit, and HRBP workflow integration that any production attrition model needs before scores reach a manager's inbox.

The data is entirely synthetic and generated in the notebook. Replace it with your own HRIS data only after completing the risk assessment template in `03-governance/risk-assessment-template.md` and reviewing with Legal and Privacy.

## What this notebook does

1. Generates a synthetic workforce of 5,000 employees with realistic distributions.
2. Engineers features that map to real attrition signals: tenure stage, time since last promotion, comp position vs. range, manager change history, engagement trend.
3. Trains two models side by side:
   - **Logistic regression** as the interpretable baseline. This is what you actually deploy when an HRBP needs to explain a score to a manager.
   - **Gradient boosting** as the performance reference. Useful for benchmarking but harder to defend in an employment context.
4. Evaluates discrimination performance (AUC) and calibration.
5. Runs a fairness audit across demographic segments using disparate impact analysis.
6. Discusses what an HRBP would actually see and do with the scores.

## What this notebook does NOT do

- It does not deploy a model. Production deployment requires data infrastructure, integration with your HRIS, monitoring, and ongoing fairness audits that are out of scope for a notebook.
- It does not justify acting on individual scores. Attrition models surface conversations; they do not replace them.
- It does not address the prediction-to-intervention gap. A risk score with no playbook for what to do about it is noise that erodes manager trust over time.

For the governance framework that wraps a model like this, see `03-governance/ai-use-policy.md` and `03-governance/risk-assessment-template.md`.

## Setup

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, brier_score_loss
from sklearn.calibration import calibration_curve

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

print('Setup complete.')
```

## Synthetic workforce generation

Generate 5,000 employees with realistic distributions. Attrition is modeled as a function of several factors with intentional non-linearities and interactions that resemble real HR data patterns.

In real use, this entire section is replaced by a query against your HRIS. The features below are the ones that consistently show predictive value across organizations.

```python
N = 5000

df = pd.DataFrame({
    'employee_id': range(1, N + 1),
    'tenure_months': np.clip(np.random.exponential(scale=36, size=N), 1, 240).astype(int),
    'age': np.clip(np.random.normal(38, 10, N), 22, 65).astype(int),
    'level': np.random.choice([1, 2, 3, 4, 5], N, p=[0.30, 0.30, 0.20, 0.15, 0.05]),
    'department': np.random.choice(['Engineering', 'Sales', 'Marketing', 'Customer Success', 'G&A'],
                                    N, p=[0.40, 0.20, 0.10, 0.20, 0.10]),
    'gender': np.random.choice(['F', 'M', 'NB'], N, p=[0.45, 0.53, 0.02]),
    'last_engagement_score': np.clip(np.random.normal(7.2, 1.5, N), 1, 10).round(1),
    'engagement_trend': np.random.choice(['improving', 'stable', 'declining'], N, p=[0.25, 0.55, 0.20]),
    'months_since_promotion': np.clip(np.random.exponential(scale=24, size=N), 0, 120).astype(int),
    'months_since_comp_change': np.clip(np.random.exponential(scale=12, size=N), 0, 60).astype(int),
    'comp_vs_midpoint_pct': np.clip(np.random.normal(0, 12, N), -30, 30).round(1),
    'manager_changes_last_year': np.random.choice([0, 1, 2, 3], N, p=[0.65, 0.25, 0.08, 0.02]),
    'remote_status': np.random.choice(['remote', 'hybrid', 'office'], N, p=[0.35, 0.45, 0.20]),
})

df.head()
```

### Generating the attrition outcome

The synthetic outcome is driven by a logistic combination of features. Tenure has a non-linear effect (highest risk at 12-36 months). Engagement trend matters more than absolute score. Comp position matters less than time since last comp change (recency, not absolute).

```python
def attrition_logit(row):
    score = -2.5

    if 12 <= row['tenure_months'] <= 36:
        score += 1.2
    elif row['tenure_months'] < 12:
        score += 0.4
    elif row['tenure_months'] > 120:
        score -= 0.6

    trend_effects = {'improving': -0.8, 'stable': 0.0, 'declining': 1.1}
    score += trend_effects[row['engagement_trend']]
    score += -0.15 * (row['last_engagement_score'] - 7)

    if row['months_since_promotion'] > 36:
        score += 0.6
    if row['months_since_comp_change'] > 18:
        score += 0.5

    score += 0.4 * row['manager_changes_last_year']

    if row['comp_vs_midpoint_pct'] < -10:
        score += 0.4

    dept_effects = {'Sales': 0.5, 'Customer Success': 0.2, 'Engineering': 0.0,
                    'Marketing': 0.1, 'G&A': -0.1}
    score += dept_effects[row['department']]

    return score

df['logit'] = df.apply(attrition_logit, axis=1)
df['attrition_prob'] = 1 / (1 + np.exp(-df['logit']))
df['will_attrit'] = (np.random.random(N) < df['attrition_prob']).astype(int)

print(f'Synthetic attrition rate: {df["will_attrit"].mean():.1%}')
```

## Feature engineering

The raw fields above need transformation before they become useful model inputs. Most attrition signal lives in derived features, not raw values.

```python
feature_df = pd.get_dummies(df, columns=['department', 'engagement_trend', 'remote_status'],
                            prefix=['dept', 'trend', 'work'], drop_first=True)

feature_df['tenure_under_12mo'] = (feature_df['tenure_months'] < 12).astype(int)
feature_df['tenure_12_to_36mo'] = ((feature_df['tenure_months'] >= 12) &
                                    (feature_df['tenure_months'] <= 36)).astype(int)
feature_df['tenure_over_10yr'] = (feature_df['tenure_months'] > 120).astype(int)

feature_df['promo_stale'] = (feature_df['months_since_promotion'] > 36).astype(int)
feature_df['comp_stale'] = (feature_df['months_since_comp_change'] > 18).astype(int)
feature_df['underpaid'] = (feature_df['comp_vs_midpoint_pct'] < -10).astype(int)

exclude_cols = ['employee_id', 'gender', 'logit', 'attrition_prob', 'will_attrit']
feature_cols = [c for c in feature_df.columns if c not in exclude_cols]

print(f'Total features: {len(feature_cols)}')
print('Note: gender is intentionally EXCLUDED from features. Retained only for the post-hoc fairness audit.')
```

## Train both models

We train a logistic regression baseline and a gradient boosting reference. In production, the logistic model is what gets deployed because it produces explainable coefficients an HRBP can defend in a calibration conversation.

```python
X = feature_df[feature_cols]
y = feature_df['will_attrit']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=RANDOM_SEED, stratify=y
)

logit = LogisticRegression(max_iter=1000, random_state=RANDOM_SEED)
logit.fit(X_train, y_train)
logit_proba = logit.predict_proba(X_test)[:, 1]

gbm = GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=RANDOM_SEED)
gbm.fit(X_train, y_train)
gbm_proba = gbm.predict_proba(X_test)[:, 1]

print(f'Logistic regression AUC:  {roc_auc_score(y_test, logit_proba):.3f}')
print(f'Gradient boosting AUC:    {roc_auc_score(y_test, gbm_proba):.3f}')
print()
print('AUC over 0.70 is a usable signal for prioritization, not for individual decisions.')
print('Both models clear that bar. The 2-3 point gap rarely justifies the explainability loss.')
```

## What drives the score

The logistic coefficients tell you what the model is paying attention to. Use this as the foundation for any HRBP explanation of a score.

```python
coefs = pd.DataFrame({
    'feature': feature_cols,
    'coefficient': logit.coef_[0],
}).sort_values('coefficient', key=abs, ascending=False).head(10)

print('Top 10 features by absolute coefficient:')
print()
for _, row in coefs.iterrows():
    direction = 'increases risk' if row['coefficient'] > 0 else 'decreases risk'
    print(f"  {row['feature']:<30}  {row['coefficient']:+.3f}  ({direction})")
```

## Calibration

A model can have high AUC and still be uncalibrated. If your model says someone has a 30% attrition risk and the observed rate for similar employees is 60%, your scores are misleading even though the rank ordering is correct.

For attrition models specifically, calibration matters more than rank ordering. Managers will read scores as probabilities. They need to be probabilities.

```python
logit_frac, logit_mean = calibration_curve(y_test, logit_proba, n_bins=10, strategy='quantile')

print(f'Logistic Brier score: {brier_score_loss(y_test, logit_proba):.4f}  (lower is better)')
print(f'Gradient boosting Brier: {brier_score_loss(y_test, gbm_proba):.4f}')
print()
print('Calibration curve (predicted vs. observed) for the logistic model:')
print(f'  {"Predicted":<14}{"Observed":<14}{"Status"}')
for pred, obs in zip(logit_mean, logit_frac):
    gap = abs(pred - obs)
    status = 'good' if gap < 0.05 else 'check' if gap < 0.10 else 'recalibrate'
    print(f'  {pred:.2f}          {obs:.2f}          {status}')
```

## Fairness audit

The most important section of this notebook. A score-producing HR model that is not audited for disparate impact is a legal and ethical liability. Audit every release. Audit every quarter in production.

We check whether the model's recommended-action rate (score above 0.30) differs meaningfully across protected groups. The 4/5ths rule (selection rate for any group at least 80% of the highest group's rate) is the standard EEOC threshold for disparate impact.

```python
test_indices = X_test.index
audit_df = df.loc[test_indices].copy()
audit_df['score'] = logit_proba
audit_df['flagged_high_risk'] = (audit_df['score'] >= 0.30).astype(int)

print('Fairness audit: high-risk flag rate by gender')
print()
by_gender = audit_df.groupby('gender').agg(
    n=('employee_id', 'count'),
    flag_rate=('flagged_high_risk', 'mean'),
    actual_attrit_rate=('will_attrit', 'mean'),
).round(3)
print(by_gender.to_string())
print()

max_rate = by_gender['flag_rate'].max()
min_rate = by_gender['flag_rate'].min()
ratio = min_rate / max_rate if max_rate > 0 else 1.0

print(f'Min/max flag rate ratio: {ratio:.2%}')
print(f'4/5ths threshold:        80.00%')
print()
if ratio >= 0.80:
    print('PASS: 4/5ths rule satisfied.')
    print('This does NOT mean the model is fair. It means no obvious disparate impact on this segmentation.')
else:
    print('FAIL: 4/5ths rule violated. Model must not deploy until investigated.')
print()
print('Also run this analysis across: age band, department, tenure bucket, race/ethnicity if collected,')
print('and any other protected characteristic relevant to your jurisdiction.')
```

## What an HRBP actually sees

The model produces a score. The HRBP needs three things to act on it:

1. The score itself (with a calibrated interpretation).
2. The top contributing factors for that individual.
3. A recommended conversation, not a recommended action.

Below is the format that works well in production. It puts the human in the driver's seat. The model surfaces, the HRBP decides.

```python
def format_hrbp_view(employee_id):
    row_idx = audit_df[audit_df['employee_id'] == employee_id].index[0]
    emp = audit_df.loc[row_idx]
    features = feature_df.loc[row_idx, feature_cols]

    contributions = pd.Series(
        logit.coef_[0] * features.values,
        index=feature_cols
    ).sort_values(key=abs, ascending=False)

    score = emp['score']
    if score >= 0.40:
        tier = 'HIGH'
    elif score >= 0.20:
        tier = 'ELEVATED'
    else:
        tier = 'BASELINE'

    print(f'EMPLOYEE: {int(emp["employee_id"])}  |  {emp["department"]}  |  Level {int(emp["level"])}')
    print(f'TENURE: {int(emp["tenure_months"])} months')
    print()
    print(f'ATTRITION RISK SCORE: {score:.2f}   TIER: {tier}')
    print()
    print('TOP CONTRIBUTING FACTORS:')
    for feat, contrib in contributions.head(5).items():
        if abs(contrib) > 0.05:
            direction = 'increasing' if contrib > 0 else 'decreasing'
            print(f'  - {feat}: {direction} risk')
    print()
    print('SUGGESTED HRBP CONVERSATION:')
    if tier == 'HIGH':
        print('  - Schedule a stay conversation with their manager within 2 weeks.')
        print('  - Review comp position and time since last promotion before the conversation.')
        print('  - Score is a signal for a conversation, not a conclusion about the employee.')
    elif tier == 'ELEVATED':
        print('  - Watch list. No immediate action.')
        print('  - Confirm engagement signals in next pulse survey.')
    else:
        print('  - No action required.')

high_risk = audit_df[audit_df['flagged_high_risk'] == 1].sort_values('score', ascending=False)
format_hrbp_view(int(high_risk.iloc[0]['employee_id']))
```

## Governance non-negotiables before deploying

Before scores from a model like this reach a single manager:

1. **Approval gate.** Run through the [risk assessment template](../03-governance/risk-assessment-template.md). This use case is medium-to-high risk and requires HR Leadership, Legal, and Privacy sign-off.

2. **Fairness audit cadence.** Quarterly at minimum. Whenever data drifts. Whenever the model is retrained. Document each audit. Failing audits halt the model.

3. **Score interpretation discipline.** Train HRBPs on what the score is and is not. A 60% score means "in similar populations, 60% departed." It does not mean "this person will probably leave." Reinforce this every quarter.

4. **No autonomous action.** No emails sent, no flags raised to managers, no compensation decisions, no PIP triggers from this score directly. The score routes to an HRBP. The HRBP decides whether to act.

5. **Employee transparency.** Employees should know that an attrition risk model exists, what data it uses, and that they can request human review of any consequential decision involving model output. This is not optional under GDPR Article 22 and increasingly required by state law.

6. **Score retention policy.** Scores are time-sensitive. Stale scores influence decisions in ways that are hard to audit. Default to deleting scores older than 90 days unless there is a specific retention reason.

7. **Manager exposure rules.** Decide who sees scores. The default should be HRBP only, with HRBPs choosing what to surface in manager conversations. Direct manager access to individual scores creates risk that the score becomes performance feedback, which it is not.

## Adapting this for your organization

1. **Replace synthetic data.** Pull the equivalent fields from your HRIS. Most are standard: tenure, level, department, performance ratings, comp position, manager history.

2. **Recalibrate the feature engineering.** The non-linear effects (tenure 12-36 months as peak risk, etc.) are reasonable defaults but your workforce may have different patterns.

3. **Set your own action threshold.** The 0.30 threshold here is illustrative. Pick yours based on what fraction of the workforce you can actually have stay conversations with each quarter.

4. **Build the HRBP workflow first, then build the model.** A perfect model with no clear workflow for what to do with scores will not move retention. A mediocre model paired with a thoughtful HRBP playbook will.

5. **Plan for failure modes.** What happens if the model is biased on a segment you have not measured? What happens if it produces a confidently wrong score that informs a stay-or-go conversation? Both will happen. Have the rollback ready.
