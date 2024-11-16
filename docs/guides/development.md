# Development Guide

## Setup Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/steganography-tool.git
cd steganography-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements/dev.txt

# Install pre-commit hooks
pre-commit install
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_steganography.py -k "test_dct"

# Run with coverage
pytest --cov=src tests/
```

## Code Style

- Follow PEP 8
- Use type hints
- Write docstrings (Google style)
- Maximum line length: 79 characters
- Run black before committing

## Contributing

1. Fork repository
2. Create feature branch
3. Make changes
4. Add tests
5. Run linters
6. Submit pull request

## Building Documentation

```bash
# Install sphinx
pip install sphinx sphinx-rtd-theme

# Build docs
cd docs
make html
``` 