# Lab 01 — Authentication Log Analysis

**Security+ domain:** Security Operations  
**Difficulty:** Beginner–Intermediate

## Scenario

The SOC has received an alert for repeated failed SSH logins. Analyze a simulated authentication log, identify suspicious sources, and produce a short incident triage summary.

## Objectives

- Parse authentication events.
- Identify repeated failures.
- Distinguish failed and successful activity.
- Create indicators of compromise (IOCs).
- Recommend containment and follow-up actions.

## Prerequisites

- Python 3.8+

## Part 1 — Review the Dataset

```bash
cat data/sample_auth.log
```

Look for failed password events, successful login events, source IP addresses, usernames, and time clustering.

## Part 2 — Run the Analyzer

```bash
python3 scripts/log_analyzer.py data/sample_auth.log
```

The script counts failed authentication attempts by source IP.

## Part 3 — Triage

Treat any source with **5 or more failures** as suspicious for this lab.

| Source IP | Failed Attempts | Successful Login? | Priority |
|---|---:|---|---|
| | | | |

## Part 4 — Incident Response Mapping

Map your actions to:

1. Preparation
2. Detection and analysis
3. Containment
4. Eradication
5. Recovery
6. Lessons learned

Possible containment actions include temporarily blocking a suspicious source, disabling a targeted account if compromise is suspected, requiring a credential reset, reviewing MFA logs, and searching other systems for the same source IP.

## Part 5 — Write a Triage Summary

Include:

- What happened
- When it happened
- Which accounts were targeted
- Suspicious source IPs
- Whether a successful login followed failures
- Recommended next action

## Verification

Explain:

- Why repeated failures alone do not prove compromise.
- Why a success after many failures deserves higher priority.
- Why timestamps and centralized logging matter.
- Why containment should preserve evidence when possible.

## Portfolio Summary

> Analyzed simulated Linux authentication logs with Python, identified repeated login failures, generated source-IP indicators, and mapped findings to incident-response containment and recovery actions.
