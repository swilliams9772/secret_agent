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

- **LSB (Least Significant Bit)**
  - Modifies least significant bits of pixel values
  - Higher storage capacity (up to 12.5% of image size)
  - Faster processing speed
  - Ideal for larger payloads

### Security Features
- **Strong Encryption**
  - Fernet symmetric encryption (AES-128)
  - Random salt generation per operation
  - PBKDF2 key derivation with SHA-256
  - 200,000 iteration rounds

- **Data Integrity**
  - CRC32 checksum verification
  - Length prefix encoding
  - Corruption detection
  - Format validation

### User Interfaces
- **Web Interface (Streamlit)**
  - Modern, responsive design
  - Real-time capacity estimation
  - Progress tracking
  - File previews
  - Drag-and-drop support
  - Dark/light theme

- **Desktop GUI (Tkinter)**
  - Native application feel
  - Image preview capability
  - Method selection
  - Quality control

## 📦 Installation

### Prerequisites
- Python 3.8+
- Required packages:
  ```bash
  pip install -r requirements.txt
  ```

### Quick Start 