# Lab 1.1: Threat Modeling & Analysis

## 🎯 Lab Objectives

By completing this lab, you will:
- ✅ Understand threat modeling methodologies
- ✅ Identify threats to a system
- ✅ Map attack vectors
- ✅ Assess risk levels
- ✅ Recommend mitigation strategies

---

## ⏱️ Time Requirement

- **Estimated Duration**: 2-3 hours
- **Difficulty Level**: Beginner
- **Prerequisites**: Understanding of threat actors and vulnerability types

---

## 📋 Lab Scenario

You are a security consultant hired by **TechCorp Inc.**, a mid-sized SaaS company offering project management software.

**Company Information:**
- 500 employees (200 technical staff)
- 10,000 active users
- Cloud infrastructure (AWS)
- Customer data including sensitive project information
- Payment processing integration

**Your Task**: Conduct a threat model for their customer portal application.

---

## 🛠️ Lab Requirements

### Tools Needed
- Text editor (VS Code, Sublime, etc.)
- Threat modeling tool (optional):
  - Microsoft Threat Modeling Tool (free)
  - Draw.io (free, browser-based)
  - Lucidchart (paid)
- MITRE ATT&CK framework access

### Files to Create
- `threat_model.md` - Your threat model documentation
- `risk_matrix.xlsx` - Risk assessment spreadsheet
- `mitigation_plan.txt` - Recommended mitigations

---

## 📚 Background Information

### Threat Modeling Methodologies

**STRIDE Model** (Microsoft)
- **S**poofing - Identity spoofing
- **T**ampering - Data modification
- **R**epudiation - Deny actions
- **I**nformation Disclosure - Data exposure
- **D**enial of Service - Service unavailability
- **E**levation of Privilege - Unauthorized access

**PASTA Model** (Tactical)
- Process for Attack Simulation and Threat Analysis
- 7-step methodology
- Focused on risk-driven approach

### Risk Calculation
```
Risk = Likelihood × Impact × Vulnerability

Where:
- Likelihood: 1-5 (1=unlikely, 5=very likely)
- Impact: 1-5 (1=minimal, 5=critical)
- Vulnerability: 1-5 (1=well-defended, 5=poorly defended)
```

---

## 🔄 Step-by-Step Instructions

### Step 1: Identify Assets (30 minutes)

List all assets that need protection:

```markdown
## Assets Inventory

### Data Assets
- Customer project data
- User credentials
- Payment information
- API keys and tokens
- Session tokens

### System Assets
- Web application servers
- Database servers
- Authentication service
- API gateway
- Payment gateway

### Infrastructure Assets
- AWS EC2 instances
- RDS databases
- S3 buckets
- Load balancers
- CDN services
```

**Your Task**: Identify at least 15 assets in the TechCorp system.

---

### Step 2: Identify Threat Actors (30 minutes)

Determine which threat actors are relevant:

```markdown
## Relevant Threat Actors

### Nation-State Actors
- Likelihood: Low
- Motivation: Industrial espionage
- Capabilities: High
- Risk Level: Medium (low likelihood, high impact)

### Cybercriminals
- Likelihood: High
- Motivation: Financial gain (ransom, data theft)
- Capabilities: Medium-High
- Risk Level: High

### Competitors
- Likelihood: Medium
- Motivation: Business intelligence
- Capabilities: Medium
- Risk Level: Medium

### Insiders
- Likelihood: Low-Medium
- Motivation: Financial, revenge
- Capabilities: High (internal access)
- Risk Level: High
```

**Your Task**: Create a similar analysis for TechCorp's relevant threat actors.

---

### Step 3: Identify Threats (1 hour)

List potential threats using STRIDE model:

```markdown
## STRIDE Analysis

### Spoofing (Identity Spoofing)
- Threat: Attacker impersonates legitimate user
- Attack Vector: Credential phishing, MFA bypass
- Likelihood: High
- Impact: High
- Vulnerability: Session hijacking possible

### Tampering (Data Modification)
- Threat: Attacker modifies customer project data
- Attack Vector: Man-in-the-middle, SQL injection
- Likelihood: Medium
- Impact: Critical
- Vulnerability: Weak input validation

### Repudiation
- Threat: User denies performing an action
- Attack Vector: Lack of audit logging
- Likelihood: Low
- Impact: Medium
- Vulnerability: Incomplete logging

### Information Disclosure
- Threat: Unauthorized access to sensitive data
- Attack Vector: SQL injection, insecure APIs
- Likelihood: High
- Impact: Critical
- Vulnerability: Insufficient encryption

### Denial of Service
- Threat: Service becomes unavailable
- Attack Vector: DDoS, application crashes
- Likelihood: Medium
- Impact: High
- Vulnerability: No rate limiting

### Elevation of Privilege
- Threat: User gains admin access
- Attack Vector: Privilege escalation vuln
- Likelihood: Low
- Impact: Critical
- Vulnerability: Insufficient access controls
```

**Your Task**: Complete STRIDE analysis for TechCorp's customer portal (6+ threats per category).

---

### Step 4: Create Threat Model Diagram (45 minutes)

Create a data flow diagram (DFD) showing:
1. External entities (users, admins, payment processor)
2. Processes (authentication, data processing)
3. Data stores (databases, caches)
4. Data flows (arrows showing data movement)

**Example DFD Elements**:
```
[External Entity] → [Process] → [Data Store]

User → Login Process → User Database
        ↓
    Auth Service
        ↓
    Session Token
        ↓
    [User Portal]
```

**Your Task**: 
- Draw a DFD for TechCorp's system
- Identify at least 10 data flows
- Label each with data type and direction

---

### Step 5: Map Attack Vectors (45 minutes)

For each identified threat, document:
- Attack vector
- Entry point
- Path to impact
- Required privileges
- Detection difficulty

**Example**:
```markdown
### Attack Vector: SQL Injection on Search Function

**Threat**: Information Disclosure
**Attack Method**: Input malicious SQL in search box
**Entry Point**: Web application search field
**Path**: Search input → Query builder → Database
**Required Privileges**: None (public user)
**Detection Difficulty**: Medium (unusual SQL syntax)
**Impact**: Database compromise, data exfiltration
**Likelihood**: High (common vulnerability)
```

**Your Task**: Document attack vectors for 8+ threats.

---

### Step 6: Risk Assessment (45 minutes)

Calculate risk scores using the formula:
```
Risk Score = Likelihood (1-5) × Impact (1-5) × Vulnerability (1-5)
Maximum Score = 125
Risk Rating:
- 0-25: Low
- 26-60: Medium
- 61-100: High
- 101-125: Critical
```

**Create a Risk Matrix**:

```markdown
| Threat | Likelihood | Impact | Vulnerability | Risk Score | Priority |
|--------|-----------|--------|----------------|-----------|----------|
| Credential Theft | 5 | 5 | 4 | 100 | Critical |
| SQL Injection | 4 | 5 | 3 | 60 | High |
| DDoS Attack | 3 | 4 | 2 | 24 | Low |
| Data Exfiltration | 4 | 5 | 4 | 80 | High |
| Privilege Escalation | 2 | 5 | 3 | 30 | Medium |
```

**Your Task**: Create a risk matrix for all identified threats.

---

### Step 7: Develop Mitigation Strategies (1 hour)

For each High/Critical risk, recommend:

1. **Control Type**
   - Technical (firewall, encryption)
   - Administrative (policies, training)
   - Physical (locks, cameras)

2. **Mitigation Strategy**
   - Prevention (reduce likelihood/vulnerability)
   - Detection (early warning)
   - Response (minimize impact)

**Example Mitigations**:

```markdown
### Threat: Credential Theft

**Prevention Controls**:
- Implement MFA on all accounts
- Enforce strong password policies
- Use security keys for admins

**Detection Controls**:
- Monitor for suspicious login patterns
- Alert on multiple failed attempts
- Track unusual geographic access

**Response Controls**:
- Incident response playbook
- Password reset procedures
- Compromise notification process

**Estimated Cost**: $15,000 implementation
**Risk Reduction**: 70% (from score 100 to 30)
**Implementation Timeline**: 2 months
```

**Your Task**: Create mitigation strategies for top 5 risks.

---

## 📊 Lab Deliverables

### 1. Threat Model Document
File: `threat_model.md`

**Include:**
- Executive summary
- Assets inventory
- Threat actor analysis
- STRIDE threat list
- Attack vector mappings
- Data flow diagram
- Risk assessment matrix

**Length**: 10-15 pages

### 2. Risk Assessment Spreadsheet
File: `risk_matrix.xlsx`

**Include:**
- All identified threats
- Risk calculations
- Prioritization
- Visualizations (charts)
- Summary statistics

### 3. Mitigation Plan
File: `mitigation_plan.txt`

**Include:**
- Top 10 risks
- Recommended controls
- Implementation timeline
- Cost estimates
- Responsible parties

---

## 🔍 Verification Checklist

Before submitting your lab, verify:

- [ ] At least 15 assets identified
- [ ] All 6 STRIDE categories analyzed
- [ ] At least 12 unique threats documented
- [ ] Attack vectors mapped for each threat
- [ ] Risk scores calculated for all threats
- [ ] Risks prioritized by severity
- [ ] Mitigation strategies for top 5 risks
- [ ] Data flow diagram created
- [ ] All documentation is clear and detailed
- [ ] Format is professional and organized

---

## 💡 Lab Tips

1. **Be Thorough**: Don't skip any STRIDE category
2. **Think Like Attacker**: What would you exploit?
3. **Consider Multiple Paths**: One asset may have many threats
4. **Real-World Focus**: Use actual attack methods from MITRE ATT&CK
5. **Risk Prioritization**: Focus on high-likelihood, high-impact threats
6. **Control Balance**: Mix prevention, detection, and response

---

## 🚀 Advanced Variations

### Extended Lab Options

1. **Create Incident Response Plan**
   - Response procedures for each threat
   - Playbook creation
   - Recovery procedures

2. **Threat Intelligence Integration**
   - Research actual CVEs affecting the stack
   - Map CVEs to identified threats
   - Add known exploit information

3. **Multi-Scenario Analysis**
   - Analyze threat models for different departments
   - Consider insider threat scenarios
   - Model advanced persistent threats

4. **Security Control Assessment**
   - Evaluate existing controls
   - Identify control gaps
   - Create remediation roadmap

---

## 📚 Reference Materials

### Tools
- [Microsoft Threat Modeling Tool](https://microsoft.com/threat-modeling-tool)
- [Draw.io (Free Diagram Tool)](https://draw.io)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)

### Frameworks
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [NIST Risk Management](https://nvlpubs.nist.gov/)
- [ISO 31000 Risk Management](https://www.iso.org/iso-31000-risk-management.html)

---

## ✅ Success Criteria

Your lab will be successful if:

- ✅ Threat model is comprehensive and covers all major systems
- ✅ Risk assessment is accurate and well-documented
- ✅ Mitigations are practical and cost-effective
- ✅ Documentation is clear and professional
- ✅ Analysis demonstrates understanding of threats

---

## 🎓 Learning Outcomes

After completing this lab, you will:
- Understand threat modeling process
- Identify threats systematically
- Calculate and prioritize risks
- Recommend appropriate controls
- Create security improvement plans

---

**Completion Status**: Ready to Start ✓

**Next Lab**: [Lab 1.2: Vulnerability Assessment](./lab_02_vuln_assessment.md)

---

*Lab Created: August 2026*  
*Difficulty: Beginner to Intermediate*
