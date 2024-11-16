from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements/base.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="steganography-tool",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive steganography toolkit with multiple interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/steganography-tool",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Security :: Cryptography",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "pytest-cov>=2.12.1",
            "black>=21.7b0",
            "isort>=5.9.3",
            "flake8>=3.9.2",
            "mypy>=0.910",
            "sphinx>=4.1.2",
            "pre-commit>=2.15.0",
        ],
        "test": [
            "pytest>=6.2.5",
            "pytest-cov>=2.12.1",
            "coverage>=5.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "stego-cli=steganography.cli:main",
            "stego-gui=interfaces.desktop.app:main",
            "stego-web=interfaces.web.app:main",
        ],
    },
) 