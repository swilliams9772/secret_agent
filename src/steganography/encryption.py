from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from .exceptions import EncryptionError

def generate_key(password: str, salt: bytes = None) -> tuple[bytes, bytes]:
    """Generate encryption key from password with optional salt"""
    try:
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=200000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return salt, key
    except Exception as e:
        raise EncryptionError(f"Key generation failed: {str(e)}")

def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt data using Fernet with random salt"""
    try:
        salt, key = generate_key(password)
        f = Fernet(key)
        encrypted = f.encrypt(data)
        return salt + encrypted
    except Exception as e:
        raise EncryptionError(f"Encryption failed: {str(e)}")

def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    """Decrypt data using stored salt"""
    try:
        salt, encrypted = encrypted_data[:16], encrypted_data[16:]
        _, key = generate_key(password, salt)
        f = Fernet(key)
        return f.decrypt(encrypted)
    except Exception as e:
        raise EncryptionError(f"Decryption failed: {str(e)}") 