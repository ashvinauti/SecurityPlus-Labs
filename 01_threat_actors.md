# Domain 1.1: Threat Actors & Attributes

## 📋 Overview

Threat actors are individuals or groups that conduct cyberattacks. Understanding their characteristics, motivations, and capabilities is essential for security professionals.

---

## 🎯 Learning Objectives

After studying this section, you should be able to:
- ✅ Identify different types of threat actors
- ✅ Explain motivations and capabilities by actor type
- ✅ Describe attack sophistication levels
- ✅ Understand nation-state actor behaviors
- ✅ Recognize insider threat characteristics

---

## 👥 Types of Threat Actors

### 1. Nation-States

**Characteristics:**
- Highest skill level and resources
- State-sponsored cyber operations
- Advanced persistent threat (APT) capability
- Long-term strategic objectives

**Motivations:**
- Espionage and intelligence gathering
- Political advantage
- Critical infrastructure disruption
- Cyber warfare capabilities

**Examples:**
- APT28 (Russia) - Fancy Bear
- APT29 (Russia) - Cozy Bear
- Lazarus Group (North Korea)
- Comment Crew (China)

**Mitigation:**
- Advanced threat detection systems
- Threat intelligence sharing
- Zero trust architecture
- Incident response capabilities

---

### 2. Cybercriminals

**Characteristics:**
- Motivated by financial gain
- Operate criminal organizations
- Focus on exploitable vulnerabilities
- Prefer high-impact, quick returns

**Motivations:**
- Direct financial theft
- Ransomware campaigns
- Identity theft
- Credential harvesting

**Attack Methods:**
- Phishing campaigns
- Malware distribution
- Ransomware deployment
- Card fraud and skimming

**Mitigation:**
- User awareness training
- Email filtering and DLP
- Regular backups
- Incident response plans

---

### 3. Hacktivists

**Characteristics:**
- Motivated by ideology or social causes
- Variable skill levels
- Often operate publicly
- Use attacks to make political statements

**Motivations:**
- Social justice causes
- Environmental concerns
- Political activism
- Anti-government protests

**Attack Methods:**
- Website defacement
- DDoS attacks
- Data leaks (doxxing)
- Public disclosure campaigns

**Notable Groups:**
- Anonymous
- LulzSec
- WikiLeaks associates

**Mitigation:**
- Incident communication planning
- Public relations preparedness
- DDoS protection
- Legal response readiness

---

### 4. Insiders

**Characteristics:**
- Have legitimate system access
- May be current or former employees
- Often have elevated privileges
- Hardest threat to detect

**Motivations:**
- Revenge (disgruntled employees)
- Financial incentives (bribery)
- Espionage (foreign agents)
- Ideological reasons

**Risk Factors:**
- Disengagement from organization
- Financial difficulties
- Lack of oversight
- Excessive privileges

**Attack Methods:**
- Data exfiltration
- System sabotage
- Credential sharing
- Malware installation

**Mitigation:**
- Principle of least privilege
- Access monitoring and logging
- Behavior analytics
- Employee awareness
- Background checks
- Exit procedures

---

### 5. Competitors/Industrial Spies

**Characteristics:**
- Target business intelligence
- Often sophisticated
- Focused on specific industries
- May work with insiders

**Motivations:**
- Trade secret theft
- Competitive advantage
- Market intelligence
- Patent/product development info

**Attack Methods:**
- Targeted spear phishing
- Social engineering
- Dumpster diving
- Insider recruitment

**Mitigation:**
- Trade secret protection
- Physical security
- Counterintelligence programs
- Secure development practices

---

## 🎭 Threat Actor Attributes

### Skill Levels

**Unskilled Attackers**
- Script kiddies using pre-made tools
- Limited technical knowledge
- Random, opportunistic attacks
- Easy to detect and stop

**Semi-Skilled Attackers**
- Can modify existing exploits
- Understand basic networking/coding
- More focused campaigns
- Require better defenses

**Skilled Attackers**
- Can find and exploit zero-days
- Sophisticated methodologies
- Targeted campaigns
- Advanced evasion techniques

**Highly Skilled Attackers**
- Nation-state level capabilities
- Develop custom exploits
- Multi-year campaigns
- Expert evasion and persistence

### Motivation Levels

**Low Motivation**
- Casual interest
- Testing skills
- Entertainment
- One-off attempts

**Medium Motivation**
- Financial incentive
- Political cause
- Competitive advantage
- Personal vendetta

**High Motivation**
- Strategic government objective
- Survival incentive
- Ideological commitment
- Critical business threat

---

## 📊 Attack Sophistication Framework

```
Sophistication Level | Skills | Resources | Detection Difficulty
─────────────────────┼────────┼──────────┼──────────────────
Minimal              | Basic  | Low      | Very Easy
Low                  | Limited| Low-Med  | Easy
Medium               | Good   | Medium   | Moderate
High                 | Expert | High     | Difficult
Very High            | Elite  | Very High| Very Difficult
```

---

## 🌐 Common Threat Actor Campaigns

### APT Campaign Characteristics

1. **Initial Compromise**
   - Spear phishing
   - Watering hole attacks
   - Supply chain compromise

2. **Persistence**
   - Backdoor installation
   - Credential theft
   - Lateral movement

3. **Exfiltration**
   - Data theft over time
   - Encrypted channels
   - Steganography use

4. **Cleanup**
   - Log deletion
   - Evidence removal
   - Backdoor removal (sometimes)

---

## 🔍 Identifying Threat Actors

### MITRE ATT&CK Framework

The MITRE ATT&CK framework documents threat actor techniques:

**Enterprise Tactics:**
- Reconnaissance
- Resource Development
- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Defense Evasion
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Command & Control
- Exfiltration
- Impact

**How to Use:**
- Map observed behaviors to techniques
- Identify threat actor TTPs (Tactics, Techniques, Procedures)
- Develop defensive controls
- Improve detection capabilities

---

## 📈 Threat Actor Evolution

### Trends in Threat Actor Behavior

**Increased Sophistication**
- Use of AI/ML in attacks
- Custom malware development
- Supply chain targeting

**Ransomware Evolution**
- From data deletion → data encryption → data theft
- Double extortion tactics
- Targeting critical infrastructure

**Supply Chain Attacks**
- SolarWinds
- Kaseya
- 3CX

**Geopolitical Factors**
- Nation-state competition
- Sanctions and retaliation
- Regional conflicts

---

## 🛡️ Defense Strategies by Actor Type

### Against Nation-States
- Advanced threat detection (AI/ML)
- Threat intelligence integration
- Zero trust implementation
- Incident response capabilities

### Against Cybercriminals
- Strong authentication (MFA)
- Regular security updates
- User awareness training
- Backup and recovery

### Against Hacktivists
- Robust DDoS protection
- Crisis communication plans
- Social media monitoring
- Public relations readiness

### Against Insiders
- Least privilege access
- User behavior analytics
- Data loss prevention
- Regular audits

---

## 💾 Key Takeaways

- **Different threat actors** have different motivations and capabilities
- **Nation-states** are most dangerous but least common
- **Cybercriminals** are most common and profit-focused
- **Insiders** are hardest to detect and prevent
- **Multi-factor approach** needed against diverse threats
- **Threat intelligence** helps identify specific actors
- **Layered defenses** required against skilled attackers

---

## 🧪 Hands-On Exercise

### Exercise 1.1: Threat Actor Analysis

**Scenario**: Your organization is a financial services company. You've detected suspicious activity indicating multiple threat actors.

**Tasks**:
1. Identify which type(s) of threat actor would target financial institutions
2. Explain their likely motivations
3. Describe what data they might target
4. Recommend defensive controls for each actor type
5. Create an incident response plan

**Deliverable**: Write a 1-2 page threat assessment document

---

## 📚 Further Reading

- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Cyber Threat Coalition Reports](https://www.cyberthreatcoalition.org/)
- [Mandiant Threat Intelligence](https://www.mandiant.com/)
- [CrowdStrike Global Threat Report](https://www.crowdstrike.com/)

---

## ✅ Review Questions

1. What are the key differences between nation-state and cybercriminal threat actors?
2. Explain why insider threats are considered high-risk
3. What is the MITRE ATT&CK framework and how is it used?
4. How would your defensive strategy differ for APT vs ransomware gangs?
5. What are indicators of a sophisticated vs unskilled attacker?

---

**Next**: Read [02_vulnerability_types.md](./02_vulnerability_types.md) to understand vulnerabilities targeted by these actors.

---

*Last Updated: August 2026*
