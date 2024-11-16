import numpy as np
import cv2
import os
from pathlib import Path

def generate_test_images():
    """Generate test carrier images of different sizes and types"""
    data_dir = Path(__file__).parent
    
    # Create test images of different sizes
    sizes = [
        (100, 100),    # Small
        (800, 600),    # Medium
        (1920, 1080),  # Full HD
        (3840, 2160)   # 4K
    ]
    
    for width, height in sizes:
        # Create random color image
        img = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
        
        # Save in different formats
        cv2.imwrite(str(data_dir / f"carrier_{width}x{height}.png"), img)
        cv2.imwrite(str(data_dir / f"carrier_{width}x{height}.jpg"), img)
        cv2.imwrite(str(data_dir / f"carrier_{width}x{height}.bmp"), img)

def generate_test_payloads():
    """Generate test payload data of different types and sizes"""
    data_dir = Path(__file__).parent
    
    # Text files
    text_samples = {
        'small': "Hello, World! This is a test message.",
        'medium': "Lorem ipsum " * 100,
        'large': "Test content " * 1000
    }
    
    for size, content in text_samples.items():
        with open(data_dir / f"payload_{size}.txt", 'w') as f:
            f.write(content)
    
    # Binary files
    binary_sizes = {
        'small': 1024,        # 1KB
        'medium': 102400,     # 100KB
        'large': 1024000      # 1MB
    }
    
    for size, bytes_count in binary_sizes.items():
        data = os.urandom(bytes_count)
        with open(data_dir / f"payload_{size}.bin", 'wb') as f:
            f.write(data)

if __name__ == "__main__":
    generate_test_images()
    generate_test_payloads() 