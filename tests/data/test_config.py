"""Test configuration and constants"""

# Test file paths
TEST_CARRIERS = {
    'small': 'carrier_100x100.png',
    'medium': 'carrier_800x600.png',
    'large': 'carrier_1920x1080.png',
    '4k': 'carrier_3840x2160.png'
}

TEST_PAYLOADS = {
    'text_small': 'payload_small.txt',
    'text_medium': 'payload_medium.txt',
    'binary_small': 'payload_small.bin',
    'binary_medium': 'payload_medium.bin',
    'binary_large': 'payload_large.bin'
}

# Test parameters
TEST_PASSWORDS = [
    'simple123',
    'Complex!P@ssw0rd',
    '超级密码123',
    '!@#$%^&*()',
    'very_long_password_for_testing_purposes'
]

TEST_METHODS = ['dct', 'lsb']

TEST_QUALITIES = [0.1, 0.5, 0.9, 1.0]

# Expected capacities (in bytes)
EXPECTED_CAPACITIES = {
    'small_dct': 1024,      # 1KB
    'small_lsb': 3750,      # ~3.7KB
    'medium_dct': 15360,    # 15KB
    'medium_lsb': 180000,   # ~175KB
    'large_dct': 62500,     # ~61KB
    'large_lsb': 750000     # ~732KB
}

# Error messages
ERROR_MESSAGES = {
    'capacity': "Data too large for carrier image",
    'password': "Invalid password or corrupted data",
    'format': "Unsupported image format",
    'quality': "Quality must be between 0.1 and 1.0",
    'method': "Unsupported steganography method"
}

# Test timeouts (seconds)
TIMEOUTS = {
    'small': 5,
    'medium': 15,
    'large': 30,
    '4k': 60
} 