# Windows installation script for steganography tool

# Check Python version
$python_version = python -c "import sys; print('.'.join(map(str, sys.version_info[:2])))"
$required_version = "3.8"

if ([version]$python_version -lt [version]$required_version) {
    Write-Error "Error: Python $required_version or higher is required"
    exit 1
}

# Create virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate

# Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies..."
pip install -r requirements/base.txt

Write-Host "Installation complete!"
Write-Host "Activate the virtual environment with: .\venv\Scripts\Activate" 