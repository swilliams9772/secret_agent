# API Documentation

## Core Module (steganography.core)

### SteganoExfil Class

Main class for steganography operations.

#### Methods

##### hide_data
```python
def hide_data(data: bytes, carrier_image_path: str, output_path: str, 
              password: str, method: str = 'dct', quality: float = None) -> None
```
Hide data in carrier image.

**Parameters:**
- `data`: Raw bytes to hide
- `carrier_image_path`: Path to carrier image
- `output_path`: Where to save result
- `password`: Encryption password
- `method`: 'dct' or 'lsb'
- `quality`: Image quality (0.1-1.0)

##### extract_data
```python
def extract_data(stego_image_path: str, password: str, method: str = 'dct') -> bytes
```
Extract hidden data from stego image.

**Parameters:**
- `stego_image_path`: Path to stego image
- `password`: Decryption password  
- `method`: Must match hide method

## Encryption Module (steganography.encryption)

### Functions

##### encrypt_data
```python
def encrypt_data(data: bytes, password: str) -> bytes
```
Encrypt data using Fernet with random salt.

##### decrypt_data  
```python
def decrypt_data(encrypted_data: bytes, password: str) -> bytes
```
Decrypt data using stored salt.

## Utils Module (steganography.utils)

### Functions

##### add_error_detection
```python
def add_error_detection(data: bytes) -> bytes
```
Add CRC32 checksum for error detection.

##### verify_error_detection
```python
def verify_error_detection(data: bytes) -> bytes
```
Verify CRC32 checksum and return data. 