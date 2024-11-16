from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def generate_key(password: str) -> bytes:
    """Generate encryption key from password with random salt"""
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return salt + key

def encrypt_data(data: bytes, password: str) -> bytes:
    """Encrypt data using Fernet with random salt"""
    key_data = generate_key(password)
    salt, key = key_data[:16], key_data[16:]
    f = Fernet(key)
    return salt + f.encrypt(data)

def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    """Decrypt data using stored salt"""
    salt, encrypted = encrypted_data[:16], encrypted_data[16:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    return f.decrypt(encrypted) 