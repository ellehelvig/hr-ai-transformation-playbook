# Claims not yet in the registry

Every dated or status-bearing regulatory claim found in `03-governance` that does not yet
have a record in this directory. Listed so the gap is countable rather than invisible.

A claim leaves this list when it has a record with a real primary-source URL. It becomes
trustworthy when that record carries a verbatim quote and a `last_verified` date.

Two things block most of these: the primary-source URL has to be confirmed rather than
guessed, and the verbatim quote has to be pulled from a fetch of the real document.
Guessing a statute URL is exactly the failure this registry exists to prevent, so these
stay listed until someone resolves them properly.

## European Union

- Commission draft Guidelines on high-risk classification under Article 6, published
  19 May 2026, consultation closed 23 July 2026, final text expected around end of 2026.
  Draft and non-binding. `03-governance/README.md`, `eu-ai-act-intake-template.md`
- EDPS and EDPB statement at a July 2026 Parliament conference that the Omnibus delay
  creates no GDPR safe harbor. `deployer-checklist.md`, `eu-ai-act-intake-template.md`
- EDPB 2026 Coordinated Enforcement Framework covering GDPR Articles 12 to 14 across
  roughly 25 national DPAs. `deployer-checklist.md`, `eu-ai-act-intake-template.md`
- CJEU SCHUFA standard: a vendor whose score the employer heavily relies on can itself be
  the Article 22 controller. `eu-ai-act-intake-template.md`
- Most member states missed the 7 June 2026 pay transparency transposition deadline.
  `pay-equity-governance.md`

## United States, federal

- EEOC withdrew its May 2022 and May 2023 AI technical assistance documents in early 2025.
  `03-governance/README.md`, `ai-use-policy.md`
- Executive Order 14179 directed agencies to suspend Biden-era AI policy guidance.
  `03-governance/README.md`
- Executive Order "Restoring Equality of Opportunity and Meritocracy", 23 April 2025,
  directs agencies to deprioritize disparate-impact enforcement. `03-governance/README.md`,
  `ai-use-policy.md`, `risk-assessment-template.md`
- Title VII disparate-impact liability remains codified and privately enforceable.
  `03-governance/README.md`, `ai-use-policy.md`
- Mobley v. Workday as the template case for AI hiring discrimination claims against
  vendors. `risk-assessment-template.md`

## United States, states

- Illinois HB 3773 amendments to the Illinois Human Rights Act. `03-governance/README.md`
- Colorado SB 24-205 repealed and reenacted by SB 26-189 in May 2026 as the Automated
  Decision-Making Technology Act, effective 1 January 2027 with narrower scope.
  `03-governance/README.md`, `risk-assessment-template.md`
- Colorado enforcement of both SB 24-205 and SB 26-189 stayed by a federal magistrate in
  April 2026 pending a ruling on xAI's constitutional challenge and completion of AG
  rulemaking due by 1 January 2027. `risk-assessment-template.md`
- California FEHA algorithmic discrimination rules, effective October 2025.
  `03-governance/README.md`, `risk-assessment-template.md`
- California CPPA ADMT regulations, effective January 2027. `03-governance/README.md`,
  `risk-assessment-template.md`
- California AB 1883 and SB 947 pending the Governor's signature with a
  30 September 2026 deadline. `risk-assessment-template.md`
- California SB 1162 pay data reporting as amended by SB 464: filing deadline the second
  Wednesday of May, per-establishment filing, mandatory civil penalties and demographic
  data separation effective 1 January 2026, and the 23-category SOC classification
  starting with the 2026 cycle due May 2027. `pay-equity-governance.md`
- At least 17 states plus DC have active pay transparency laws as of 2026.
  `pay-equity-governance.md`
- New Jersey LAD disparate-impact standard as applied to automated decision-making tools:
  prohibited unless necessary to achieve a substantial, legitimate, nondiscriminatory interest
  with no less discriminatory alternative, and whether the employer tested the tool for bias
  may be weighed as relevant evidence. The January 2025 DCR guidance states this but rests it
  on 56 N.J.R. 969(a), a rulemaking notice that has not been fetched, so the claim is asserted
  in prose without its own anchored record. `risk-assessment-template.md`,
  `04-enablement/hr-ai-literacy-curriculum.md`
- New Jersey DCR disparate-impact rules. The January 2025 guidance cites them as proposed at
  56 N.J.R. 969(a) (proposed section 13:16-3.2). Secondary reporting says DCR has since
  adopted them. The adoption date and the N.J.A.C. citation are unverified against the New
  Jersey Register, so no repo file asserts either. Resolve before any file cites the adopted
  rules. Not currently asserted anywhere.
- Connecticut Public Act 26-15 Section 8(a): the developer owes the deployer supporting
  information only where the technology was advertised, marketed, configured, contracted
  for, sold or licensed to materially influence an employment-related decision. The vendor
  checklist leans on that scoping. `vendor-intake-checklist.md`
- Connecticut Public Act 26-15 Sections 9 and 10: deployer interaction disclosure and
  pre-decision written notice, attaching to technology deployed on or after 1 October 2027.
  `04-enablement/hr-ai-literacy-curriculum.md`
- Connecticut Public Act 26-15 Section 12: violations are CUTPA unfair or deceptive trade
  practices, enforced solely by the Attorney General, with no private right of action and a
  60-day cure for violations on or before 31 December 2027.
  `04-enablement/hr-ai-literacy-curriculum.md`
- Connecticut Public Act 26-15 Section 26: employers serving a federal WARN notice must
  disclose to the Connecticut Labor Department whether the layoffs relate to AI or other
  technological change. `04-enablement/hr-ai-literacy-curriculum.md`

## United Kingdom and Canada

- Data (Use and Access) Act 2025. `README.md` regulatory coverage section
- Ontario disclosure rule for AI use in publicly advertised job postings.
  `README.md` regulatory coverage section

## Standards, not law

These are referenced as frameworks rather than legal obligations, so they need a lighter
record or none at all. Decide before registering them.

- NIST AI Risk Management Framework 1.0, January 2023. `03-governance/README.md`,
  `ai-use-policy.md`
- ISO/IEC 42001. `03-governance/README.md`, `ai-use-policy.md`, `vendor-intake-checklist.md`
