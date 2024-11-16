from setuptools import setup, find_packages

setup(
    name="steganography-tool",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.19.2",
        "opencv-python>=4.5.3",
        "pillow>=8.3.1",
        "streamlit>=1.0.0",
        "cryptography>=3.4.7",
        "scipy>=1.7.1",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "pytest-cov>=2.12.1",
            "black>=21.7b0",
            "flake8>=3.9.2",
            "mypy>=0.910",
        ]
    },
    python_requires=">=3.8",
) 