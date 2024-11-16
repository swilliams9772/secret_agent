import zlib
from typing import Tuple

def add_error_detection(data: bytes) -> bytes:
    """Add CRC32 checksum for error detection"""
    checksum = zlib.crc32(data).to_bytes(4, byteorder='big')
    return checksum + data

def verify_error_detection(data: bytes) -> bytes:
    """Verify CRC32 checksum and return data without checksum"""
    checksum = int.from_bytes(data[:4], byteorder='big')
    payload = data[4:]
    if zlib.crc32(payload) != checksum:
        raise ValueError("Data corruption detected")
    return payload

def encode_data_length(data_length: int) -> bytes:
    """Encode data length as 4 bytes"""
    return data_length.to_bytes(4, byteorder='big')

def decode_data_length(length_bytes: bytes) -> int:
    """Decode data length from 4 bytes"""
    return int.from_bytes(length_bytes, byteorder='big') 