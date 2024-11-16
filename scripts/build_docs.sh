#!/bin/bash

# Documentation builder script

# Activate virtual environment
source venv/bin/activate

# Install documentation dependencies if needed
pip install sphinx sphinx-rtd-theme

# Build documentation
cd docs
make clean
make html

echo "Documentation built in docs/_build/html/" 