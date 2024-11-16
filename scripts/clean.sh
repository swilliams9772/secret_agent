#!/bin/bash

# Cleanup script

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete

# Remove test cache
find . -type d -name ".pytest_cache" -exec rm -r {} +
find . -type d -name ".coverage" -exec rm -r {} +
find . -type d -name "htmlcov" -exec rm -r {} +

# Remove build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# Remove temporary files
rm -f temp_*
rm -f *.tmp*

echo "Cleanup complete!" 