import zlib
from typing import Tuple, Union, Optional
import numpy as np
import cv2
import os
from pathlib import Path
from .exceptions import CapacityError, FormatError

def calculate_capacity(image: np.ndarray, method: str = 'dct') -> int:
    """
    Calculate maximum data capacity for given image and method
    
    Args:
        image: Carrier image array
        method: Steganography method ('dct' or 'lsb')
        
    Returns:
        int: Maximum bytes that can be hidden
    """
    if method == 'dct':
        y = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)[:,:,0]
        blocks = (y.shape[0] * y.shape[1]) // 64  # 8x8 blocks
        return int(blocks * 0.1)  # ~10% of coefficients usable
    elif method == 'lsb':
        return (image.size * 3) // 8  # 3 channels, 1 bit per channel
    else:
        raise ValueError(f"Unsupported method: {method}")

def validate_image(image_path: Union[str, Path], 
                  min_size: Tuple[int, int] = (32, 32),
                  max_size: Tuple[int, int] = (8192, 8192)) -> np.ndarray:
    """
    Validate and load image with format and size checks
    
    Args:
        image_path: Path to image file
        min_size: Minimum dimensions (width, height)
        max_size: Maximum dimensions (width, height)
        
    Returns:
        np.ndarray: Loaded and validated image
    
    Raises:
        FormatError: If image format is unsupported
        ValueError: If image dimensions are invalid
    """
    supported_formats = {'.png', '.jpg', '.jpeg', '.bmp'}
    ext = Path(image_path).suffix.lower()
    
    if ext not in supported_formats:
        raise FormatError(f"Unsupported format: {ext}")
        
    img = cv2.imread(str(image_path))
    if img is None:
        raise FormatError("Failed to load image")
        
    h, w = img.shape[:2]
    if w < min_size[0] or h < min_size[1]:
        raise ValueError(f"Image too small (min: {min_size})")
    if w > max_size[0] or h > max_size[1]:
        raise ValueError(f"Image too large (max: {max_size})")
        
    return img

def add_error_detection(data: bytes) -> bytes:
    """Add CRC32 checksum and length prefix"""
    length = len(data).to_bytes(4, byteorder='big')
    checksum = zlib.crc32(data).to_bytes(4, byteorder='big')
    return length + checksum + data

def verify_error_detection(data: bytes) -> bytes:
    """
    Verify length and CRC32 checksum
    
    Returns:
        bytes: Original data without length and checksum
    
    Raises:
        ValueError: If verification fails
    """
    if len(data) < 8:
        raise ValueError("Data too short")
        
    length = int.from_bytes(data[:4], byteorder='big')
    checksum = int.from_bytes(data[4:8], byteorder='big')
    payload = data[8:]
    
    if len(payload) != length:
        raise ValueError("Length mismatch")
    if zlib.crc32(payload) != checksum:
        raise ValueError("Checksum verification failed")
        
    return payload

def cleanup_temp_files(temp_dir: Union[str, Path], 
                      pattern: str = "stego_temp_*") -> None:
    """Clean up temporary files"""
    temp_path = Path(temp_dir)
    for f in temp_path.glob(pattern):
        try:
            f.unlink()
        except OSError:
            pass 