#!/bin/bash

# Development environment setup script

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install development dependencies
echo "Installing development dependencies..."
pip install -r requirements/dev.txt

# Install pre-commit hooks
echo "Setting up pre-commit hooks..."
pre-commit install

# Create necessary directories
echo "Creating project directories..."
mkdir -p src/steganography/tests/{unit,integration,data}
mkdir -p docs/{api,guides,images}

echo "Development setup complete!" 