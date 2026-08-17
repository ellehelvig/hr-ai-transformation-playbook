# Skills gap analysis

This notebook identifies skills gaps across a workforce by comparing employee skill profiles against role competency requirements. It surfaces priority development areas at the individual, team, and organizational level, and ends in an L&D investment prioritization output.

The data is entirely synthetic and generated in the notebook. Replace it with your own skill assessment data only after completing the [risk assessment template](../03-governance/risk-assessment-template.md), skills gap data is sensitive, and access should be restricted to L&D and HRBPs.

## What this notebook does

1. Defines a competency framework: required proficiency by role and skill.
2. Loads employee skill profiles (synthetic here, your assessment data in production).
3. Computes gap scores at the individual level, then aggregates by team, function, and level.
4. Identifies the highest-priority org-wide development needs.
5. Produces an L&D investment prioritization output, weighted by reach and severity.

## What this notebook does NOT do

- It does not tell you why a gap exists. Low proficiency can mean a training gap, a hiring gap, or a role that outgrew the person in it. The notebook flags where, not why.
- It does not account for strategic importance. A skill with a moderate gap score can still be the organization's top priority if it's newly critical to the business. Layer in strategic weighting before finalizing an L&D budget.
- It does not replace manager judgment on individual development plans. Aggregate priority tiers inform where to invest; they don't tell an HRBP what to say to a specific employee.

For the governance framework that wraps an analysis like this, see [ai-use-policy.md](../03-governance/ai-use-policy.md) and [risk-assessment-template.md](../03-governance/risk-assessment-template.md).

## Setup

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
```

## 1. Define the competency framework

Replace this with your organization's actual competency framework. It defines what skills are required at each role and level, and at what proficiency.

**Proficiency scale:**
- 1 = Awareness (knows the concept)
- 2 = Developing (can apply with guidance)
- 3 = Proficient (applies independently)
- 4 = Expert (coaches others, sets direction)

```python
# Format: {role: {skill: required_proficiency_level}}

COMPETENCY_FRAMEWORK = {
    'Software Engineer L3': {
        'Python': 3, 'System Design': 2, 'Code Review': 3,
        'Communication': 2, 'Project Management': 1, 'Data Analysis': 2,
        'Security Practices': 2, 'CI/CD': 2, 'Mentoring': 1
    },
    'Software Engineer L4': {
        'Python': 4, 'System Design': 3, 'Code Review': 4,
        'Communication': 3, 'Project Management': 2, 'Data Analysis': 3,
        'Security Practices': 3, 'CI/CD': 3, 'Mentoring': 2
    },
    'HR Business Partner': {
        'Employee Relations': 3, 'Data Analysis': 2, 'Communication': 4,
        'Project Management': 3, 'Change Management': 3, 'Coaching': 3,
        'Employment Law': 2, 'AI Literacy': 2, 'Mentoring': 2
    },
    'Engineering Manager': {
        'Python': 2, 'System Design': 3, 'Communication': 4,
        'Project Management': 4, 'Data Analysis': 3, 'Coaching': 3,
        'Security Practices': 2, 'Mentoring': 4, 'Change Management': 2
    },
    'Recruiter': {
        'Communication': 4, 'Data Analysis': 2, 'Project Management': 2,
        'Employment Law': 2, 'AI Literacy': 2, 'Coaching': 1,
        'Change Management': 1, 'Mentoring': 1, 'Employee Relations': 1
    }
}

all_skills = sorted(set(skill for role in COMPETENCY_FRAMEWORK.values() for skill in role))
print(f'Roles in framework: {len(COMPETENCY_FRAMEWORK)}')
print(f'Skills tracked: {len(all_skills)}')
```

## 2. Load employee skill profiles

Replace the synthetic generator with your actual skill assessment export: a skills survey, performance system self-assessments, LMS completion data mapped to skills, or manager assessments. Expected format is one row per employee, a column per skill (rated 0 to 4), plus employee ID, role, department, manager, and tenure.

```python
def generate_synthetic_profiles(n=150):
    """Synthetic employee skill profiles for development only."""
    roles = list(COMPETENCY_FRAMEWORK.keys())
    role_weights = [0.35, 0.25, 0.15, 0.15, 0.10]
    departments = {
        'Software Engineer L3': 'Engineering', 'Software Engineer L4': 'Engineering',
        'HR Business Partner': 'People', 'Engineering Manager': 'Engineering',
        'Recruiter': 'People'
    }
    records = []
    for i in range(n):
        role = np.random.choice(roles, p=role_weights)
        required = COMPETENCY_FRAMEWORK[role]
        tenure = int(np.random.gamma(3, 12))
        skill_levels = {}
        for skill in all_skills:
            req = required.get(skill, 0)
            if req == 0:
                skill_levels[skill] = np.random.choice([0, 1], p=[0.6, 0.4])
            else:
                base = req - np.random.choice([0, 1, 2], p=[0.4, 0.4, 0.2])
                skill_levels[skill] = max(0, min(4, base + (1 if tenure > 24 else 0)))
        records.append({
            'employee_id': f'EMP{i+1:04d}', 'role': role, 'department': departments[role],
            'tenure_months': tenure, **skill_levels
        })
    return pd.DataFrame(records)

df = generate_synthetic_profiles()
print(f'Employees: {len(df):,}')
print(df['role'].value_counts())
```

## 3. Compute individual gap scores

Gap is the shortfall between required and actual proficiency. Only deficits count, exceeding a requirement isn't a gap.

```python
def compute_gap(row, skill):
    required = COMPETENCY_FRAMEWORK.get(row['role'], {}).get(skill, 0)
    actual = row.get(skill, 0)
    return max(0, required - actual)

gap_cols = []
for skill in all_skills:
    col = f'gap_{skill}'
    df[col] = df.apply(lambda row: compute_gap(row, skill), axis=1)
    gap_cols.append(col)

df['total_gap_score'] = df[gap_cols].sum(axis=1)
df['skills_at_gap'] = (df[gap_cols] > 0).sum(axis=1)

print('Employees with zero gaps:', (df['total_gap_score'] == 0).sum())
print('Employees with 3+ skill gaps:', (df['skills_at_gap'] >= 3).sum())
```

## 4. Org-wide priority gaps

Which skills have the most widespread gaps across the organization, not just the biggest individual gaps.

```python
gap_summary = pd.DataFrame({
    'skill': all_skills,
    'employees_with_gap': [(df[f'gap_{s}'] > 0).sum() for s in all_skills],
    'avg_gap_size': [df[f'gap_{s}'].mean().round(2) for s in all_skills],
    'pct_workforce_affected': [(df[f'gap_{s}'] > 0).mean().round(3) * 100 for s in all_skills]
}).sort_values('employees_with_gap', ascending=False)

print(gap_summary.head(10).to_string(index=False))

fig, ax = plt.subplots(figsize=(10, 5))
top_gaps = gap_summary.head(8)
ax.barh(top_gaps['skill'], top_gaps['pct_workforce_affected'], color='#185FA5', alpha=0.85)
ax.set_xlabel('% of workforce with a gap in this skill')
ax.set_title('Priority skills gaps, % of workforce affected', fontsize=13)
ax.invert_yaxis()
plt.tight_layout()
plt.show()
```

## 5. Gap heatmap by role

Average gap by role and skill, shows where each team specifically needs development, which the org-wide view alone can hide.

```python
role_skill_gaps = df.groupby('role')[[f'gap_{s}' for s in all_skills]].mean()
role_skill_gaps.columns = all_skills

fig, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(role_skill_gaps, annot=True, fmt='.1f', cmap='YlOrRd', linewidths=0.5, ax=ax,
            cbar_kws={'label': 'Avg gap (0 = no gap, 3 = large gap)'})
ax.set_title('Average skill gap by role', fontsize=13)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```

## 6. L&D investment prioritization

Score each skill for investment priority: high reach (many people affected) plus high severity (large average gap) is the highest priority, not just the biggest average gap on its own.

```python
gap_summary['reach_score'] = gap_summary['pct_workforce_affected'] / gap_summary['pct_workforce_affected'].max()
gap_summary['severity_score'] = gap_summary['avg_gap_size'] / gap_summary['avg_gap_size'].max()
gap_summary['priority_score'] = (0.6 * gap_summary['reach_score'] + 0.4 * gap_summary['severity_score']).round(3)

gap_summary['priority_tier'] = pd.cut(
    gap_summary['priority_score'], bins=[0, 0.33, 0.66, 1.01],
    labels=['Tier 3, monitor', 'Tier 2, plan', 'Tier 1, invest now']
)

priority_output = gap_summary[[
    'skill', 'employees_with_gap', 'pct_workforce_affected', 'avg_gap_size', 'priority_score', 'priority_tier'
]].sort_values('priority_score', ascending=False)

print(priority_output.to_string(index=False))
priority_output.to_csv('ld_investment_priorities.csv', index=False)
```

## Governance non-negotiables before acting on this

1. **Validate data quality.** Skill self-assessments are notoriously biased in both directions, people over-rate and under-rate their own skills. Calibrate with manager assessments or objective measures where possible.

2. **Weight by strategic importance, not just gap size.** A skill with a moderate gap score can still be the top investment priority if it just became critical to the business. The priority tiers here are a starting point, not the final word.

3. **Check for equity before publishing.** Run gap scores by demographic group. If one group consistently shows higher gaps, the more likely explanation is unequal access to development opportunities, not a skill deficit, investigate before drawing conclusions.

4. **Restrict individual-level access.** Individual gap data goes to HRBPs for their own teams, not to managers directly without HR review, and never broadly shared. Aggregate, team-level, and org-level views can go wider.

5. **Pair with cost before building the business case.** Gap data alone doesn't justify an L&D budget. Pair it with the cost of the gap, lost productivity, attrition risk, project delays, to make the investment case.

## Adapting this for your organization

1. **Replace the competency framework** with your organization's actual role and skill requirements, ideally owned by L&D and validated by function leaders, not reverse-engineered from job descriptions.
2. **Replace synthetic profiles** with your real assessment data, joined from whatever system captures it (survey tool, performance system, LMS).
3. **Recalibrate the priority formula's weights.** The 0.6/0.4 reach-to-severity split here is a reasonable default; your organization may weight severity higher if a small number of deep gaps matter more than broad shallow ones.
4. **Decide the refresh cadence.** Skills change faster than most HRIS refresh cycles account for. Quarterly is a reasonable default; annual is too slow to catch a skill that just became critical.
