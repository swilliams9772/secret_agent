#!/bin/bash

# Test runner script

# Activate virtual environment
source venv/bin/activate

# Run tests with coverage
echo "Running tests with coverage..."
pytest tests/ --cov=src --cov-report=html

# Run linting
echo "Running linters..."
flake8 src/ tests/
black --check src/ tests/
mypy src/ tests/

# Show test coverage report
echo "Test coverage report:"
coverage report 