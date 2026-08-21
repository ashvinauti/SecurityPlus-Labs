# Lab 01 — Network Segmentation Design

**Security+ domain:** Security Architecture  
**Difficulty:** Intermediate

## Scenario

A small company currently uses one flat network for employee workstations, servers, administrators, and guest devices. Design a segmented architecture that limits lateral movement and applies least privilege.

## Objectives

- Design security zones based on trust level and function.
- Create allow/deny traffic rules.
- Apply default-deny and least-privilege principles.
- Explain how segmentation reduces blast radius.

## Proposed Zones

| Zone | Subnet | Purpose |
|---|---|---|
| User VLAN | 10.10.10.0/24 | Employee endpoints |
| Server VLAN | 10.10.20.0/24 | Internal application servers |
| Admin VLAN | 10.10.30.0/24 | Privileged administration |
| Guest VLAN | 10.10.40.0/24 | Untrusted guest devices |
| DMZ | 10.10.50.0/24 | Internet-facing services |

## Task 1 — Draw the Trust Boundaries

Create a diagram showing:

```text
Internet
   |
Firewall
   |
   +-- DMZ
   |
Core / L3 Firewall
   +-- User VLAN
   +-- Server VLAN
   +-- Admin VLAN
   +-- Guest VLAN
```

Annotate where authentication, filtering, monitoring, and logging occur.

## Task 2 — Build a Traffic Matrix

| Source | Destination | Service | Action | Reason |
|---|---|---|---|---|
| User | Server | HTTPS/443 | Allow | Business application |
| User | Admin | Any | Deny | Prevent privilege-zone access |
| Guest | Internal RFC1918 | Any | Deny | Isolation |
| Admin | Server | SSH/22 | Allow | Administration |
| Internet | DMZ | HTTPS/443 | Allow | Public web service |
| DMZ | Server | Required app port only | Conditional allow | Application dependency |

## Task 3 — Apply Security Principles

For each principle, write one implementation:

- Least privilege
- Default deny
- Defense in depth
- Zero Trust
- Fail secure
- Network access control

## Task 4 — Threat Analysis

Explain how segmentation affects:

1. Malware on a guest laptop
2. Compromise of a user workstation
3. Compromise of a DMZ web server
4. Stolen administrator credentials

## Validation Questions

- Which zone should have the fewest inbound paths?
- Why should guest devices never route freely to internal networks?
- Why is a DMZ not trusted?
- Where would you place IDS/IPS monitoring?

## Evidence to Capture

- Network diagram
- Completed traffic matrix
- Four threat-analysis responses
- Short paragraph explaining blast-radius reduction

## Portfolio Summary

> Designed a segmented five-zone enterprise network and documented least-privilege firewall flows, trust boundaries, DMZ controls, and lateral-movement mitigations.
