class SteganoError(Exception):
    """Base exception for steganography operations"""
    pass

class CapacityError(SteganoError):
    """Raised when data exceeds carrier capacity"""
    pass

class FormatError(SteganoError):
    """Raised for unsupported or invalid formats"""
    pass

class EncryptionError(SteganoError):
    """Raised for encryption/decryption failures"""
    pass

class ValidationError(SteganoError):
    """Raised for input validation failures"""
    pass

class ExtractionError(SteganoError):
    """Raised when data extraction fails"""
    pass

class ConfigError(SteganoError):
    """Raised for configuration errors"""
    pass

class IntegrityError(SteganoError):
    """Raised for data integrity verification failures"""
    pass 