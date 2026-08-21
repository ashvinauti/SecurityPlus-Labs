#!/bin/bash
#
# Security+ Labs - Environment Setup Script
# Initializes directories, installs dependencies, and validates setup
#

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_FILE="$REPO_ROOT/setup.log"

# Functions
print_header() {
    echo -e "\n${BLUE}╔════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${NC} $1"
    echo -e "${BLUE}╚════════════════════════════════════════════╝${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Main setup
main() {
    print_header "Security+ Labs Environment Setup"
    
    # Initialize log
    echo "Setup started at $(date)" > "$LOG_FILE"
    log "Repository root: $REPO_ROOT"
    
    # Check Python version
    print_header "Checking Python Installation"
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 is not installed"
        log "ERROR: Python3 not found"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    print_success "Python $PYTHON_VERSION found"
    log "Python version: $PYTHON_VERSION"
    
    # Check Git
    print_header "Checking Git Installation"
    
    if ! command -v git &> /dev/null; then
        print_warning "Git is not installed (optional for lab)"
        log "WARNING: Git not found"
    else
        print_success "Git found: $(git --version)"
        log "Git: $(git --version)"
    fi
    
    # Create directory structure
    print_header "Creating Directory Structure"
    
    DIRS=(
        "$REPO_ROOT/certs"
        "$REPO_ROOT/labs-docker"
        "$REPO_ROOT/lab-data"
        "$REPO_ROOT/resources"
        "$REPO_ROOT/1_Threats_Vulnerabilities/labs/scripts"
        "$REPO_ROOT/1_Threats_Vulnerabilities/exercises"
        "$REPO_ROOT/2_Architecture_Design/labs/scripts"
        "$REPO_ROOT/2_Architecture_Design/exercises"
        "$REPO_ROOT/3_Implementation/labs/scripts"
        "$REPO_ROOT/3_Implementation/exercises"
        "$REPO_ROOT/4_Operations_Incident_Response/labs/scripts"
        "$REPO_ROOT/4_Operations_Incident_Response/exercises"
        "$REPO_ROOT/5_Governance_Risk_Compliance/labs/scripts"
        "$REPO_ROOT/5_Governance_Risk_Compliance/exercises"
    )
    
    for dir in "${DIRS[@]}"; do
        mkdir -p "$dir" 2>/dev/null
        if [ -d "$dir" ]; then
            print_success "Created: $(basename $dir)"
            log "Directory created: $dir"
        fi
    done
    
    # Create .gitkeep files
    print_header "Setting Up Git Tracking"
    
    for dir in "${DIRS[@]}"; do
        touch "$dir/.gitkeep"
    done
    
    print_success "Added .gitkeep files"
    log "Git tracking initialized"
    
    # Set up Python virtual environment
    print_header "Setting Up Python Virtual Environment"
    
    if [ ! -d "$REPO_ROOT/venv" ]; then
        python3 -m venv "$REPO_ROOT/venv"
        print_success "Virtual environment created"
        log "Virtual environment created"
    else
        print_warning "Virtual environment already exists"
    fi
    
    # Source venv
    source "$REPO_ROOT/venv/bin/activate"
    print_success "Virtual environment activated"
    log "Virtual environment activated"
    
    # Upgrade pip
    print_header "Installing Python Dependencies"
    
    pip install --quiet --upgrade pip setuptools wheel
    print_success "Pip upgraded"
    log "Pip upgraded"
    
    # Install requirements
    if [ -f "$REPO_ROOT/requirements.txt" ]; then
        pip install --quiet -r "$REPO_ROOT/requirements.txt"
        print_success "Dependencies installed from requirements.txt"
        log "Dependencies installed"
    else
        print_warning "requirements.txt not found"
        log "WARNING: requirements.txt not found"
    fi
    
    # Make scripts executable
    print_header "Setting File Permissions"
    
    find "$REPO_ROOT/scripts" -name "*.sh" -exec chmod +x {} \; 2>/dev/null
    find "$REPO_ROOT/scripts" -name "*.py" -exec chmod +x {} \; 2>/dev/null
    find "$REPO_ROOT/*/scripts" -name "*.sh" -exec chmod +x {} \; 2>/dev/null
    find "$REPO_ROOT/*/scripts" -name "*.py" -exec chmod +x {} \; 2>/dev/null
    
    print_success "Scripts made executable"
    log "File permissions set"
    
    # Check for security issues
    print_header "Security Validation"
    
    if [ -f "$REPO_ROOT/.env" ]; then
        print_warning ".env file found - ensure it's in .gitignore"
        log "WARNING: .env file exists"
    else
        print_success "No .env file detected (good)"
    fi
    
    if [ -f "$REPO_ROOT/.gitignore" ]; then
        print_success ".gitignore file found"
        log ".gitignore present"
    else
        print_warning ".gitignore not found"
        log "WARNING: .gitignore not found"
    fi
    
    # Verify installation
    print_header "Verifying Installation"
    
    echo "Python: $(python3 --version)"
    echo "Pip: $(pip --version | awk '{print $2}')"
    log "Verification: Python $(python3 --version | awk '{print $2}'), Pip $(pip --version | awk '{print $2}')"
    
    # Test imports
    python3 << EOF
try:
    import requests
    import paramiko
    import cryptography
    print("✓ Core packages imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
EOF
    
    # Summary
    print_header "Setup Summary"
    
    echo "Environment Setup Completed Successfully!"
    echo ""
    echo "Repository: $REPO_ROOT"
    echo "Virtual Env: $REPO_ROOT/venv"
    echo "Log File: $LOG_FILE"
    echo ""
    echo "Next steps:"
    echo "  1. Source the virtual environment:"
    echo "     source $REPO_ROOT/venv/bin/activate"
    echo ""
    echo "  2. Read the getting started guide:"
    echo "     cat $REPO_ROOT/GETTING_STARTED.md"
    echo ""
    echo "  3. Review the domains:"
    echo "     cat $REPO_ROOT/DOMAINS_OVERVIEW.md"
    echo ""
    echo "  4. Start with Domain 1:"
    echo "     cd $REPO_ROOT/1_Threats_Vulnerabilities"
    echo ""
    
    log "Setup completed successfully"
}

# Run main
main
