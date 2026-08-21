# Getting Started with Security+ Labs

This guide will walk you through setting up the Security+ repository and lab environment.

## ⚙️ Prerequisites

Before you start, ensure you have:

### Required
- **Python 3.8 or higher**
  ```bash
  python3 --version
  ```
- **Git**
  ```bash
  git --version
  ```
- **Bash shell** (Linux, macOS, or WSL2 on Windows)

### Optional (for advanced labs)
- **Docker & Docker Compose** (for containerized lab environments)
  ```bash
  docker --version
  docker-compose --version
  ```
- **VMware/VirtualBox** (for network lab simulations)
- **Network tools**: `nmap`, `tcpdump`, `openssl`

---

## 📥 Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/yourusername/SecurityPlus-Labs.git

# Navigate into the directory
cd SecurityPlus-Labs

# Verify structure
ls -la
```

---

## 🔧 Step 2: Set Up Python Virtual Environment

It's recommended to use a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Linux/macOS:
source venv/bin/activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# On Windows (CMD):
venv\Scripts\activate.bat
```

**Verify activation**: Your prompt should show `(venv)` prefix

---

## 📦 Step 3: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installations
pip list
```

### What Gets Installed
- **paramiko**: SSH automation
- **pycryptodome**: Cryptography operations
- **requests**: HTTP library for API calls
- **pyyaml**: YAML parsing
- **python-nmap**: Network scanning
- **netaddr**: IP address manipulation
- **jinja2**: Templating engine
- **colorama**: Colored terminal output

---

## 🚀 Step 4: Run Initial Setup Script

```bash
# Make setup script executable
chmod +x scripts/setup_lab_environment.sh

# Run setup
bash scripts/setup_lab_environment.sh
```

This script will:
- ✅ Create necessary directories
- ✅ Download sample data files
- ✅ Initialize lab environment
- ✅ Set up file permissions
- ✅ Verify all dependencies

**Expected output**: Setup complete ✓

---

## 📚 Step 5: Navigate the Repository

### Main Folders

```
SecurityPlus-Labs/
├── 1_Threats_Vulnerabilities/     ← Domain 1 studies & labs
├── 2_Architecture_Design/          ← Domain 2 studies & labs
├── 3_Implementation/               ← Domain 3 studies & labs
├── 4_Operations_Incident_Response/ ← Domain 4 studies & labs
├── 5_Governance_Risk_Compliance/   ← Domain 5 studies & labs
├── labs-docker/                    ← Docker environments
├── scripts/                        ← Utility scripts
└── resources/                      ← Quick references & checklists
```

### Recommended First Steps

1. **Read the overview**
   ```bash
   cat DOMAINS_OVERVIEW.md
   ```

2. **Check your setup**
   ```bash
   python3 scripts/setup_lab_environment.sh --verify
   ```

3. **Start with Domain 1**
   ```bash
   cd 1_Threats_Vulnerabilities
   cat 01_threat_actors.md
   ```

---

## 🐳 Step 6: Set Up Docker Environment (Optional)

If you want to use containerized labs:

```bash
# Navigate to docker directory
cd labs-docker

# Build Docker images
docker-compose build

# Start containers
docker-compose up -d

# Verify containers are running
docker-compose ps

# Access a container
docker exec -it vulnerable-app bash

# Stop containers
docker-compose down -v
```

---

## 🧪 Step 7: Run Your First Lab

### Lab 1.1: Threat Modeling

```bash
# Navigate to first domain
cd 1_Threats_Vulnerabilities/labs

# Read lab instructions
cat lab_01_threat_modeling.md

# Follow the step-by-step guide
# Complete the exercises in the accompanying worksheet
```

### Lab 3.1: SSL/TLS Setup

```bash
# Navigate to implementation domain
cd 3_Implementation/labs

# Read lab instructions
cat lab_01_ssl_tls_setup.md

# Run the certificate generation script
bash ../scripts/ssl_cert_generator.sh

# Verify certificates were created
ls -la ../certs/
```

---

## ✅ Verification Steps

### Verify Python Environment
```bash
# Should show virtual environment path
which python3

# Should show packages installed
pip list | grep -i "paramiko\|requests"
```

### Verify Scripts
```bash
# Check if scripts are executable
ls -l scripts/*.sh

# Test a simple script
python3 scripts/generate_study_guide.py --help
```

### Verify Docker (if installed)
```bash
docker --version
docker-compose --version
docker images
```

---

## 🔐 Environment Configuration

### Create .env File (Optional)

For labs that need API keys or credentials:

```bash
# Create environment file
cat > .env << EOF
# Lab Configuration
LAB_NETWORK=192.168.126.0/24
DOCKER_REGISTRY=your-registry
VERBOSE_MODE=true

# API Keys (if using external services)
SHODAN_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
EOF

# Protect the file
chmod 600 .env
```

**Note**: Never commit `.env` file to Git!

---

## 📖 Study Recommendations

### Beginner Path (40-50 hours)
1. **Week 1**: Threats & Vulnerabilities (20%)
2. **Week 2**: Architecture & Design (20%)
3. **Week 3**: Implementation Part 1 (25% - first half)
4. **Week 4**: Implementation Part 2 + Operations (25% + 20%)
5. **Week 5**: Governance & Compliance (15%)
6. **Week 6**: Review & Practice Exams

### Intermediate Path (30-40 hours)
- Skip basics, focus on advanced topics
- Deep dive into labs
- Complete all exercises
- Take practice exams

### Expert Path (20-30 hours)
- Review complex scenarios
- Work through difficult labs
- Contribute improvements to repository
- Prepare exam study guides

---

## 🔄 Daily Workflow

### Suggested Daily Study Routine

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Navigate to domain folder
cd 2_Architecture_Design

# 3. Read theory notes
cat 01_network_architecture.md

# 4. Work through lab
cd labs
# Follow step-by-step instructions
bash ../scripts/network_topology_creator.py

# 5. Complete exercises
cat ../exercises/design_secure_network.md
# Document your answers

# 6. Review quick reference
cat ../../resources/quick_reference.md

# 7. Deactivate environment when done
deactivate
```

---

## 🆘 Troubleshooting

### Python Version Mismatch
```bash
# If you get Python version errors
python3 --version  # Should be 3.8+

# On some systems, try:
python --version
```

### Permission Denied on Scripts
```bash
# Make scripts executable
chmod +x scripts/*.sh
chmod +x scripts/*.py

# Or use bash explicitly
bash scripts/setup_lab_environment.sh
```

### Docker Connection Issues
```bash
# Check if Docker daemon is running
sudo systemctl status docker

# Start Docker
sudo systemctl start docker

# Add user to docker group (if needed)
sudo usermod -aG docker $USER
```

### Module Not Found Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall requirements
pip install --upgrade -r requirements.txt
```

### Network Lab Issues
```bash
# If labs can't reach each other, check:
# 1. Firewall rules
sudo ufw status

# 2. Network interfaces
ifconfig  # or: ip addr

# 3. Routing table
route -n
```

---

## 📊 Validation Checklist

Before starting labs, verify:

- [ ] Python 3.8+ installed
- [ ] Git installed and working
- [ ] Repository cloned successfully
- [ ] Virtual environment created
- [ ] All dependencies installed
- [ ] Setup script ran without errors
- [ ] Docker installed (optional)
- [ ] Can read markdown files
- [ ] Can execute bash scripts
- [ ] Can run Python scripts

Run validation script:
```bash
python3 scripts/validate_environment.py
```

---

## 🎯 Next Steps

1. **Read** [DOMAINS_OVERVIEW.md](./DOMAINS_OVERVIEW.md) for domain breakdown
2. **Start** with Domain 1: Threats & Vulnerabilities
3. **Work through** the first lab in each domain
4. **Complete** all exercises
5. **Take** practice exams from resources/
6. **Review** glossary and quick reference regularly

---

## 📞 Getting Help

### If Something Doesn't Work

1. **Check the logs**
   ```bash
   cat setup.log
   ```

2. **Verify your setup**
   ```bash
   python3 scripts/validate_environment.py
   ```

3. **Check GitHub Issues**
   - Search for similar problems
   - Create a new issue with:
     - Error message
     - Python version
     - OS/Linux distribution
     - Steps to reproduce

4. **Docker Issues**
   ```bash
   docker-compose logs -f
   ```

---

## 💡 Pro Tips

1. **Keep notes** as you study - create a `MY_NOTES.md` file
2. **Track progress** - mark sections completed in DOMAINS_OVERVIEW.md
3. **Use git** - commit your exercise answers to version control
4. **Practice scripts** - modify scripts to learn how they work
5. **Join communities** - Security+ study groups on Discord/Reddit
6. **Take breaks** - Cybersecurity is intense, rest helps retention

---

## ⏱️ Estimated Time Investment

| Component | Beginner | Intermediate | Expert |
|-----------|----------|--------------|--------|
| Study Notes | 25 hrs | 15 hrs | 5 hrs |
| Labs | 20 hrs | 15 hrs | 10 hrs |
| Exercises | 15 hrs | 10 hrs | 5 hrs |
| Practice Exams | 8 hrs | 5 hrs | 3 hrs |
| **Total** | **68 hrs** | **45 hrs** | **23 hrs** |

---

## 🎓 After Completion

Once you've completed the repository:

1. **Take official practice exams**
2. **Review weak areas** using glossary and checklists
3. **Schedule your exam**
4. **Use quick reference** for last-minute review
5. **Pass and celebrate!** 🎉

---

## 📝 Updates & Maintenance

Keep your repository up to date:

```bash
# Check for updates
git status

# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt

# Check for security vulnerabilities
pip list | grep -i outdated
```

---

**Ready to start learning? Begin with [DOMAINS_OVERVIEW.md](./DOMAINS_OVERVIEW.md) or go directly to Domain 1!**

---

*Last Updated: August 2026*  
*For issues and feedback: [GitHub Issues](https://github.com/yourusername/SecurityPlus-Labs/issues)*
