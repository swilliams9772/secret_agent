import pytest
from steganography.encryption import encrypt_data, decrypt_data, generate_key
from steganography.exceptions import EncryptionError

class TestEncryption:
    def test_encryption_cycle(self):
        """Test encryption and decryption cycle"""
        data = b"Test data for encryption"
        password = "test123"

        # Encrypt
        encrypted = encrypt_data(data, password)
        
        # Decrypt
        decrypted = decrypt_data(encrypted, password)

        assert decrypted == data

    def test_different_passwords(self):
        """Test encryption with different passwords"""
        data = b"Test data"
        password1 = "password1"
        password2 = "password2"

        encrypted = encrypt_data(data, password1)

        with pytest.raises(EncryptionError):
            decrypt_data(encrypted, password2)

    def test_salt_uniqueness(self):
        """Test that salts are unique"""
        password = "test123"
        salt1, _ = generate_key(password)
        salt2, _ = generate_key(password)

        assert salt1 != salt2

    def test_key_derivation(self):
        """Test key derivation with same salt"""
        password = "test123"
        salt, key1 = generate_key(password)
        _, key2 = generate_key(password, salt)

        assert key1 == key2 