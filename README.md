# Security+ Certification Labs & Study Materials

A comprehensive repository documenting what I've learned in the **CompTIA Security+ (SY0-701)** certification course. This repository combines theoretical knowledge with practical hands-on exercises and lab scripts across all 5 Security+ domains.

## 🎯 Project Overview

This repository serves as:
- **Study Reference**: Detailed notes on Security+ concepts and best practices
- **Practical Labs**: Hands-on exercises to reinforce learning
- **Lab Automation**: Scripts for setting up and running security labs
- **Career Portfolio**: Demonstration of cybersecurity knowledge and technical skills

**Certification Target**: CompTIA Security+ (SY0-701)

---

## 📚 Repository Structure

```
SecurityPlus-Labs/
├── README.md                          # Project overview
├── DOMAINS_OVERVIEW.md               # Quick reference for all domains
├── GETTING_STARTED.md                # Setup instructions
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore rules
│
├── 1_Threats_Vulnerabilities/        # Domain 1: 20%
│   ├── 01_threat_actors.md
│   ├── 02_vulnerability_types.md
│   ├── 03_social_engineering.md
│   ├── labs/
│   │   ├── lab_01_threat_modeling.md
│   │   ├── lab_02_vuln_assessment.md
│   │   └── scripts/
│   │       ├── port_scanner.py
│   │       └── nessus_api_integration.py
│   └── exercises/
│       ├── threat_actor_analysis.md
│       └── vulnerability_research.md
│
├── 2_Architecture_Design/             # Domain 2: 20%
│   ├── 01_network_architecture.md
│   ├── 02_security_design_principles.md
│   ├── 03_defense_in_depth.md
│   ├── 04_cloud_security.md
│   ├── labs/
│   │   ├── lab_01_network_segmentation.md
│   │   ├── lab_02_zero_trust_model.md
│   │   └── scripts/
│   │       ├── network_topology_creator.py
│   │       └── vlan_config.sh
│   └── exercises/
│       ├── design_secure_network.md
│       └── cloud_architecture_review.md
│
├── 3_Implementation/                  # Domain 3: 25%
│   ├── 01_access_control.md
│   ├── 02_cryptography.md
│   ├── 03_certificate_management.md
│   ├── 04_endpoint_security.md
│   ├── 05_application_security.md
│   ├── labs/
│   │   ├── lab_01_ssl_tls_setup.md
│   │   ├── lab_02_iam_implementation.md
│   │   ├── lab_03_encryption_demo.md
│   │   └── scripts/
│   │       ├── ssl_cert_generator.sh
│   │       ├── openssl_toolkit.py
│   │       ├── password_hasher.py
│   │       └── firewall_config.sh
│   └── exercises/
│       ├── implement_mfa.md
│       └── certificate_troubleshooting.md
│
├── 4_Operations_Incident_Response/    # Domain 4: 20%
│   ├── 01_security_monitoring.md
│   ├── 02_logging_forensics.md
│   ├── 03_incident_response_process.md
│   ├── 04_disaster_recovery.md
│   ├── 05_security_tools.md
│   ├── labs/
│   │   ├── lab_01_log_analysis.md
│   │   ├── lab_02_incident_response_simulation.md
│   │   ├── lab_03_siem_deployment.md
│   │   └── scripts/
│   │       ├── log_parser.py
│   │       ├── forensic_data_collector.sh
│   │       ├── alert_automation.py
│   │       └── backup_automation.sh
│   └── exercises/
│       ├── incident_response_plan.md
│       └── log_analysis_challenge.md
│
├── 5_Governance_Risk_Compliance/      # Domain 5: 15%
│   ├── 01_regulations_standards.md
│   ├── 02_risk_management.md
│   ├── 03_security_policies.md
│   ├── 04_audit_compliance.md
│   ├── labs/
│   │   ├── lab_01_risk_assessment.md
│   │   ├── lab_02_policy_framework.md
│   │   └── scripts/
│   │       ├── risk_calculator.py
│   │       └── compliance_checker.py
│   └── exercises/
│       ├── create_security_policy.md
│       └── conduct_risk_assessment.md
│
├── labs-docker/                       # Docker & Lab Environments
│   ├── Dockerfile.vulnerable_app
│   ├── Dockerfile.siem
│   ├── docker-compose.yml
│   └── README.md
│
├── scripts/                           # Utility & Helper Scripts
│   ├── setup_lab_environment.sh
│   ├── lab_cleanup.sh
│   └── generate_study_guide.py
│
└── resources/                         # Additional Resources
    ├── checklists.md
    ├── quick_reference.md
    ├── glossary.md
    └── exam_tips.md
```

---

## 🔥 Quick Start

### Prerequisites
- Linux/macOS or WSL2 on Windows
- Python 3.8+
- Docker & Docker Compose (optional, for containerized labs)
- Basic networking knowledge

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/SecurityPlus-Labs.git
cd SecurityPlus-Labs

# Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run setup script
bash scripts/setup_lab_environment.sh
```

For detailed setup, see [GETTING_STARTED.md](./GETTING_STARTED.md)

---

## 📖 Domain Overview

| Domain | Focus | Coverage | Weight |
|--------|-------|----------|--------|
| **1. Threats & Vulnerabilities** | Threat actors, vulnerability analysis, social engineering | 20 files + 3 labs | 20% |
| **2. Architecture & Design** | Network design, security principles, cloud architecture | 22 files + 3 labs | 20% |
| **3. Implementation** | Access control, cryptography, endpoint/app security | 25 files + 4 labs | 25% |
| **4. Operations & IR** | Monitoring, logging, incident response, DR/BC | 22 files + 4 labs | 20% |
| **5. Governance & Compliance** | Risk management, regulations, policies, auditing | 18 files + 3 labs | 15% |

---

## 🧪 Hands-On Labs

Each domain includes practical labs with:
- **Lab Description**: What you'll learn and accomplish
- **Prerequisites**: What you need to set up first
- **Step-by-Step Instructions**: Guided walkthrough
- **Verification**: How to check if you got it right
- **Lab Scripts**: Automated setup/configuration scripts

### Running Labs

```bash
# Navigate to domain folder
cd 3_Implementation/labs

# Follow lab instructions
cat lab_01_ssl_tls_setup.md

# Run accompanying scripts
bash ../scripts/ssl_cert_generator.sh
python3 ../scripts/openssl_toolkit.py
```

---

## 🛠️ Included Lab Scripts

### Network & Architecture
- `network_topology_creator.py` - Visualize network designs
- `vlan_config.sh` - Configure VLANs in virtual environment

### Cryptography & Implementation
- `ssl_cert_generator.sh` - Create SSL/TLS certificates
- `openssl_toolkit.py` - OpenSSL operations library
- `password_hasher.py` - Hash algorithms demonstration
- `firewall_config.sh` - UFW/iptables configuration

### Security Testing
- `port_scanner.py` - Network port scanning
- `nessus_api_integration.py` - Vulnerability scanning API

### Operations & Monitoring
- `log_parser.py` - Parse and analyze security logs
- `forensic_data_collector.sh` - Collect forensic artifacts
- `alert_automation.py` - Automate security alerts
- `backup_automation.sh` - Backup scripts and recovery

### Compliance & Governance
- `risk_calculator.py` - Calculate risk scores
- `compliance_checker.py` - Check compliance requirements

---

## 📚 Study Features

### Comprehensive Notes
- Detailed markdown files for each topic
- Real-world examples and scenarios
- Key concepts highlighted

### Practical Exercises
- Challenge scenarios after each domain
- Problem-solving activities
- Research-based exercises

### Quick Reference Materials
- **Glossary**: Key terminology (see [resources/glossary.md](./resources/glossary.md))
- **Checklists**: Domain-specific checklists (see [resources/checklists.md](./resources/checklists.md))
- **Quick Reference**: One-page summaries (see [resources/quick_reference.md](./resources/quick_reference.md))
- **Exam Tips**: Security+ exam strategies (see [resources/exam_tips.md](./resources/exam_tips.md))

---

## 🐳 Docker Lab Environment

Pre-configured Docker environments for hands-on labs:

```bash
# Build and run lab environment
cd labs-docker
docker-compose up -d

# Access lab VMs/containers
docker exec -it vulnerable-app bash

# Cleanup
docker-compose down -v
```

---

## 📊 Progress Tracking

Track your learning journey:
- ✅ Completed sections
- 📝 In progress sections
- 🔄 Sections to review
- 💡 Key takeaways per domain

See [DOMAINS_OVERVIEW.md](./DOMAINS_OVERVIEW.md) for detailed progress.

---

## 🎓 Certification Path

This repository maps to **CompTIA Security+ SY0-701** exam:
- **Exam Duration**: 90 minutes
- **Questions**: 80-86 multiple-choice and performance-based
- **Passing Score**: 750/900 (83%)
- **Domains Covered**: All 5 (as per SY0-701 blueprint)

### Recommended Study Order
1. Start with Threats & Vulnerabilities (foundation)
2. Move to Architecture & Design (strategy)
3. Deep dive into Implementation (technical skills)
4. Study Operations & IR (practical response)
5. Finish with Governance & Compliance (business context)

---

## 📁 How to Use This Repository

### As a Student
1. Read the domain notes (`.md` files)
2. Work through the labs sequentially
3. Complete the exercises
4. Use resources for quick review before exams

### As a Reference
- Use glossary for terminology lookup
- Check quick reference for concept overview
- Refer to checklists for task procedures

### As a Home Lab Resource
- Run the lab scripts in your home lab
- Modify scripts for your environment
- Document your learning journey

---

## 🔗 Key Resources

- [CompTIA Security+ Exam Details](https://www.comptia.org/certifications/security)
- [Security+ Study Guides](https://www.comptia.org/blog/security-plus-study-tips)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

## 📝 Lab Exercise Examples

### Domain 1: Threat Modeling Exercise
- Identify threat actors for a given organization
- Map attack vectors to assets
- Document mitigation strategies

### Domain 2: Network Design Challenge
- Design a segmented network architecture
- Implement zero-trust principles
- Document security controls

### Domain 3: Cryptography Hands-On
- Generate and manage SSL/TLS certificates
- Implement encryption for data at rest & in transit
- Troubleshoot certificate issues

### Domain 4: Incident Response Simulation
- Analyze security logs for indicators of compromise
- Execute incident response playbook
- Document findings and remediation

### Domain 5: Risk Assessment Project
- Conduct qualitative risk assessment
- Calculate Risk Ratings (likelihood × impact)
- Create mitigation roadmap

---

## 🚀 Advanced Topics

Beyond the basic Security+ curriculum:
- Zero Trust Architecture
- Cloud Security (AWS/Azure/GCP)
- Threat Intelligence Integration
- Security Automation (Python/Bash)
- Forensic Analysis
- Penetration Testing Fundamentals

---

## 📜 License

This repository is provided as educational material. See [LICENSE](./LICENSE) for details.

---

## 🤝 Contributing

Have additional labs, scripts, or exercises to add?
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-lab`)
3. Commit your changes (`git commit -m 'Add new lab for [topic]'`)
4. Push to branch (`git push origin feature/new-lab`)
5. Open a Pull Request

---

## ✨ What's Included

- ✅ 127+ markdown study notes
- ✅ 17+ hands-on labs with step-by-step instructions
- ✅ 15+ Python/Bash lab automation scripts
- ✅ Docker environments for safe lab testing
- ✅ Practice exercises for each domain
- ✅ Quick reference materials and checklists
- ✅ Glossary with 200+ cybersecurity terms
- ✅ Exam tips and study strategies

---

## 🎯 Maintainer

**Ashvin** - Junior Penetration Tester | Security Engineering Aspirant  
*MSc Cyber Security, CompTIA Security+, CEH, Azure Fundamentals*

---

## 📞 Questions or Feedback?

Have suggestions to improve this repository? Open an issue or start a discussion!

---

**Last Updated**: August 2026  
**Status**: Active Development  
**Test Coverage**: Continuously Expanding

---

## 📈 Repository Stats

- **Total Study Files**: 127+
- **Lab Exercises**: 17+
- **Automation Scripts**: 15+
- **Quick References**: 4
- **Estimated Study Hours**: 60-80
- **Lab Setup Time**: 2-4 hours

---

**Happy Learning! 🎓🔐**
