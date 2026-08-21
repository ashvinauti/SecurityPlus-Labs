# Lab 02 — Vulnerability Assessment and Prioritization

**Security+ domain:** Threats, Vulnerabilities, and Mitigations  
**Difficulty:** Beginner–Intermediate

## Scenario

You are a junior security analyst reviewing a small Linux web server in an isolated lab. Your task is to identify exposed services, classify findings, assign risk, and recommend mitigations.

> Only scan systems you own or have explicit permission to test. Use `127.0.0.1` or an isolated lab VM for this exercise.

## Objectives

- Identify listening TCP services.
- Distinguish exposure from vulnerability.
- Prioritize findings using likelihood and impact.
- Recommend preventive, detective, and corrective controls.
- Document evidence in a concise vulnerability report.

## Prerequisites

- Linux/macOS/WSL
- Python 3.8+
- A local test service

## Part 1 — Start a Local Test Service

```bash
mkdir -p /tmp/securityplus-web
cd /tmp/securityplus-web
echo "Security+ lab service" > index.html
python3 -m http.server 8080
```

Leave the service running.

## Part 2 — Identify Listening Ports

```bash
ss -lnt
```

If `ss` is unavailable:

```bash
netstat -an | grep LISTEN
```

Record the port, service, bound address, and whether it is expected.

## Part 3 — Test the Service

```bash
curl -I http://127.0.0.1:8080
```

Confirm that an HTTP response is returned.

## Part 4 — Risk Assessment

Assess this finding: **An administrative web service is reachable over unencrypted HTTP.**

| Factor | Score (1–5) |
|---|---:|
| Likelihood | |
| Impact | |
| Risk = Likelihood × Impact | |

Risk bands: 1–4 Low, 5–9 Moderate, 10–16 High, 17–25 Critical.

## Part 5 — Recommend Controls

Document at least one control from each category:

- **Preventive:** firewall rule, segmentation, TLS, least privilege
- **Detective:** service monitoring, log review, configuration scanning
- **Corrective:** disable unnecessary service, patch, or reconfigure

## Evidence to Capture

1. Output of `ss -lnt`
2. Output of `curl -I`
3. Completed risk table
4. Three recommended controls

## Verification

Explain:

- Why an open port is not automatically a vulnerability.
- Why plaintext administrative traffic increases risk.
- How reducing exposure changes likelihood.
- How compensating controls can reduce risk.

## Cleanup

Stop the Python HTTP server with `Ctrl+C`.

## Portfolio Summary

> Performed a controlled vulnerability assessment of a local Linux service, documented attack surface, rated findings using likelihood × impact, and proposed preventive, detective, and corrective controls.
