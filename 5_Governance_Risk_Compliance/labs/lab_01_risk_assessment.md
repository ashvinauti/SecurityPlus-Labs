# Lab 01 — Security Risk Assessment

**Security+ domain:** Security Program Management and Oversight  
**Difficulty:** Beginner

## Scenario

You are assessing risks for a small SaaS company. Create a risk register, calculate risk ratings, select treatment strategies, and identify appropriate controls.

## Objectives

- Identify assets, threats, vulnerabilities, and impacts.
- Calculate qualitative risk scores.
- Choose accept, avoid, transfer, or mitigate.
- Track residual risk.
- Distinguish risk appetite, tolerance, and threshold.

## Risk Formula

For this lab:

```text
Risk Score = Likelihood × Impact
```

Each factor uses a 1–5 scale.

| Score | Rating |
|---:|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Critical |

## Part 1 — Create a Starter Register

Build a table with the following columns:

| Risk | Asset | Threat | Vulnerability | Likelihood | Impact | Score | Treatment |
|---|---|---|---|---:|---:|---:|---|
| Credential compromise | Identity platform | Phishing | Weak or missing MFA | 4 | 5 | | |
| Customer data loss | Production database | System failure | Insufficient recovery testing | 2 | 5 | | |
| Outdated public service | Web application | Remote attacker | Delayed patching | 4 | 4 | | |
| Cloud data exposure | Object storage | Misconfiguration | Overly permissive access | 3 | 5 | | |

Calculate each score and assign a rating.

## Part 2 — Select Risk Treatments

Choose one treatment for each risk:

- **Accept** — knowingly retain the risk
- **Avoid** — stop the risky activity
- **Transfer** — shift financial or operational impact
- **Mitigate** — reduce likelihood or impact

## Part 3 — Select Controls

Examples:

| Risk | Possible Control |
|---|---|
| Credential compromise | MFA, password manager, conditional access |
| Data loss | Backups, replication, recovery testing |
| Vulnerable software | Patch management, vulnerability scanning |
| Cloud misconfiguration | CSPM, IaC review, least privilege |

## Part 4 — Calculate Residual Risk

After selecting controls, estimate the new likelihood and impact.

```text
Inherent risk = risk before controls
Residual risk = risk after controls
```

Document whether management should accept the remaining residual risk.

## Part 5 — Management Summary

Write 5–8 sentences covering:

- Highest risks
- Proposed controls
- Residual risks
- Any risk requiring management acceptance
- Recommended review frequency

## Verification

Explain:

- Inherent vs residual risk
- Risk appetite vs tolerance
- Why not every risk can be eliminated
- Why business impact matters when prioritizing remediation

## Portfolio Summary

> Built a security risk register, scored inherent and residual risks, selected treatment strategies, and linked technical controls to business impact and governance decisions.
