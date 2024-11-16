# Windows development environment setup script

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}

# Activate virtual environment
.\venv\Scripts\Activate

# Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# Install development dependencies
Write-Host "Installing development dependencies..."
pip install -r requirements/dev.txt

# Install pre-commit hooks
Write-Host "Setting up pre-commit hooks..."
pre-commit install

# Create necessary directories
Write-Host "Creating project directories..."
New-Item -ItemType Directory -Force -Path src/steganography/tests/{unit,integration,data}
New-Item -ItemType Directory -Force -Path docs/{api,guides,images}

Write-Host "Development setup complete!" 