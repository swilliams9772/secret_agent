class SteganoError(Exception):
    """Base exception for steganography errors"""
    pass

class CapacityError(SteganoError):
    """Raised when data exceeds carrier capacity"""
    pass

class FormatError(SteganoError):
    """Raised for unsupported file formats"""
    pass

class CorruptionError(SteganoError):
    """Raised when data corruption is detected"""
    pass

class EncryptionError(SteganoError):
    """Raised for encryption/decryption errors"""
    pass 