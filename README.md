# 🕵️‍♂️ Advanced Steganography Tool

A sophisticated steganography toolkit that provides multiple methods for securely hiding data within images. Built with security, performance, and usability in mind, it offers both web-based and desktop interfaces.

## 🌟 Key Features

### Steganography Methods
- **DCT (Discrete Cosine Transform)**
  - Embeds data in frequency domain coefficients
  - Higher resistance to statistical analysis
  - Better preservation of image quality
  - Suitable for sensitive data
  - Capacity: ~1-5% of image size
  - Survives JPEG compression
  - Resistant to basic image processing
  - Ideal for watermarking and sensitive data

- **LSB (Least Significant Bit)**
  - Modifies least significant bits of pixel values
  - Higher storage capacity (up to 12.5% of image size)
  - Faster processing speed
  - Perfect reconstruction of hidden data
  - Best for uncompressed formats (PNG)
  - Ideal for large payloads
  - Maximum data capacity
  - Minimal processing overhead

### Security Features
- **Strong Encryption**
  - Fernet symmetric encryption (AES-128)
  - Random salt generation per operation
  - PBKDF2 key derivation with SHA-256
  - 200,000 iteration rounds for key derivation
  - Forward secrecy with unique salts
  - Authenticated encryption (HMAC)
  - Secure against known-plaintext attacks
  - Protection against tampering

- **Data Integrity**
  - CRC32 checksum verification
  - Length prefix encoding
  - Corruption detection
  - Format validation
  - Error recovery capabilities
  - Automatic format handling
  - Integrity verification
  - Safe extraction

### User Interfaces
- **Web Interface (Streamlit)**
  - Modern, responsive design
  - Real-time capacity estimation
  - Progress tracking
  - File previews
  - Drag-and-drop support
  - Dark/light theme
  - Batch processing
  - File type detection
  - Settings persistence
  - Mobile-friendly layout

- **Desktop GUI (Tkinter)**
  - Native application feel
  - Image preview capability
  - Method selection
  - Quality control
  - Progress indication
  - Error handling
  - Multi-threading support
  - Responsive UI
  - Cross-platform compatibility
  - Offline operation

## 📦 Quick Start Guide

### Prerequisites
```bash
# Python 3.8+ required
python --version  # Should be 3.8 or higher

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```python
from steganography import SteganoExfil

# Initialize
stego = SteganoExfil()

# Hide data (DCT method - more secure)
stego.hide_data(
    data=secret_data,
    carrier_image_path='input.png',
    output_path='output.png',
    password='YourSecretPassword',
    method='dct',
    quality=0.9  # Higher quality = better security
)

# Extract data
data = stego.extract_data(
    stego_image_path='output.png',
    password='YourSecretPassword',
    method='dct'
)
```

### Launch Interfaces
```bash
# Web Interface (Recommended)
streamlit run src/streamlit_app.py

# Desktop Interface
python src/stego_gui.py
```

## 🔧 Configuration Guide

### Quality vs Capacity Trade-off

| Quality Setting | Capacity | Security | Image Quality | Use Case |
|----------------|----------|-----------|---------------|----------|
| High (0.9-1.0) | Low | Best | Excellent | Sensitive Data |
| Medium (0.5-0.8) | Medium | Good | Good | General Use |
| Low (0.1-0.4) | High | Basic | Fair | Large Files |

### Method Selection Guide

| Feature | DCT | LSB |
|---------|-----|-----|
| Security | ★★★★★ | ★★★ |
| Capacity | ★★★ | ★★★★★ |
| Speed | ★★★ | ★★★★★ |
| Image Quality | ★★★★★ | ★★★★ |
| Compression Resistance | ★★★★ | ★★ |

## 🔒 Security Best Practices

### Password Guidelines
- Minimum 12 characters
- Mix of uppercase, lowercase, numbers, symbols
- Avoid dictionary words
- Use unique passwords
- Consider password manager
- Regular password rotation

### Operational Security
- Process data locally
- Use secure channels
- Clear temporary files
- Verify recipients
- Monitor file sizes
- Check image metadata
- Use trusted carriers
- Regular security audits

## 🧪 Testing & Validation

### Run Tests
```bash
# Full test suite
python -m pytest tests/

# Specific tests
python -m pytest tests/test_steganography.py -k "test_dct"

# With coverage
python -m pytest --cov=src tests/
```

### Performance Benchmarks
```bash
# DCT Method (1MB file)
Time: ~2.5s
CPU Usage: ~60%
Memory: ~200MB

# LSB Method (1MB file)
Time: ~0.5s
CPU Usage: ~30%
Memory: ~150MB
```

## 📊 Capacity Calculator

| Image Size | DCT Capacity | LSB Capacity |
|------------|--------------|--------------|
| 1920x1080 | ~250KB | ~800KB |
| 3840x2160 | ~1MB | ~3.2MB |
| 7680x4320 | ~4MB | ~12.8MB |

## 🤝 Contributing

### Development Setup
1. Fork repository
2. Create feature branch
3. Install dev dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
4. Run tests before PR:
   ```bash
   make test
   make lint
   ```

### Code Style
- Follow PEP 8
- Type hints required
- Docstrings (Google style)
- Max line length: 79
- Unit tests for new features

## 📄 License

MIT License - see [LICENSE](LICENSE)

## ⚠️ Disclaimer

This tool is intended for:
- Digital watermarking
- Privacy protection
- Educational purposes
- Research and development
- Secure backup
- Legitimate data hiding

Users must comply with applicable laws.

## 🙏 Acknowledgments

- OpenCV team for image processing
- Streamlit team for web framework
- Cryptography.io team for security
- SciPy team for DCT implementation
- NumPy team for array operations
- PIL team for image handling
- Testing tools developers
- Open source community

## 📧 Support & Contact

- Issues: [GitHub Issues](https://github.com/swilliams9772/secret-agent/issues)
- Discussions: [GitHub Discussions](https://github.com/swilliams9772/secret-agent/discussions)
- Email: swilliams9772@gmail.com
- Documentation: [Wiki](https://github.com/swilliams9772/secret-agent/wiki)

## 📈 Project Stats

![GitHub Stars](https://img.shields.io/github/stars/swilliams9772/secret-agent)
![GitHub Forks](https://img.shields.io/github/forks/swilliams9772/secret-agent)
![GitHub Issues](https://img.shields.io/github/issues/swilliams9772/secret-agent)
![GitHub License](https://img.shields.io/github/license/swilliams9772/secret-agent)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=swilliams9772/secret-agent&type=Date)](https://star-history.com/#swilliams9772/secret-agent&Date)
