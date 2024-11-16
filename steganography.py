import numpy as np
from PIL import Image
import cv2
from scipy import fftpack
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import zlib

class SteganoExfil:
    def __init__(self):
        self.supported_formats = ['.png', '.jpg', '.jpeg', '.bmp']
        
    def _generate_key(self, password: str) -> bytes:
        """Generate encryption key from password with random salt"""
        salt = os.urandom(16)  # Random salt for each encryption
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=200000,  # Increased iterations
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return salt + key  # Return salt with key for decryption

    def _encrypt_data(self, data: bytes, password: str) -> bytes:
        """Encrypt data using Fernet with random salt"""
        key_data = self._generate_key(password)
        salt, key = key_data[:16], key_data[16:]
        f = Fernet(key)
        return salt + f.encrypt(data)  # Include salt in encrypted data

    def _decrypt_data(self, encrypted_data: bytes, password: str) -> bytes:
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

    def _prepare_carrier_image(self, image_path: str) -> np.ndarray:
        """Load and prepare carrier image with format handling"""
        ext = os.path.splitext(image_path)[1].lower()
        if ext not in self.supported_formats:
            raise ValueError(f"Unsupported format: {ext}")
        
        if ext in ['.jpg', '.jpeg']:
            # Special handling for JPEG to avoid compression artifacts
            img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            if img is None:
                raise ValueError("Could not load image")
            # Convert to PNG temporarily to preserve quality
            temp_path = image_path + '.tmp.png'
            cv2.imwrite(temp_path, img)
            img = cv2.imread(temp_path)
            os.remove(temp_path)
            return img
        
        return cv2.imread(image_path)

    def _calculate_dct_capacity(self, carrier: np.ndarray) -> int:
        """Calculate maximum number of bits that can be hidden using DCT"""
        y = cv2.cvtColor(carrier, cv2.COLOR_BGR2YCrCb)[:,:,0]
        capacity = 0
        for i in range(y.shape[0]):
            for j in range(y.shape[1]):
                if 4 <= i + j <= 8:
                    capacity += 1
        return capacity

    def _encode_data_length(self, data_length: int) -> bytes:
        """Encode data length as 4 bytes"""
        return data_length.to_bytes(4, byteorder='big')

    def _decode_data_length(self, length_bytes: bytes) -> int:
        """Decode data length from 4 bytes"""
        return int.from_bytes(length_bytes, byteorder='big')

    def _add_error_detection(self, data: bytes) -> bytes:
        """Add CRC32 checksum for error detection"""
        checksum = zlib.crc32(data).to_bytes(4, byteorder='big')
        return checksum + data

    def _verify_error_detection(self, data: bytes) -> bytes:
        """Verify CRC32 checksum and return data without checksum"""
        checksum = int.from_bytes(data[:4], byteorder='big')
        payload = data[4:]
        if zlib.crc32(payload) != checksum:
            raise ValueError("Data corruption detected")
        return payload

    def hide_data(self, data: bytes, carrier_image_path: str, 
                  output_path: str, password: str,
                  method: str = 'dct') -> None:
        """
        Hide data in carrier image using specified method
        
        Methods:
        - 'dct': Discrete Cosine Transform domain embedding
        - 'lsb': Least Significant Bit
        - 'dwt': Discrete Wavelet Transform
        """
        # Add length prefix to data
        data_with_length = self._encode_data_length(len(data)) + data
        encrypted_data = self._encrypt_data(data_with_length, password)
        
        # Load carrier image
        carrier = self._prepare_carrier_image(carrier_image_path)
        
        # Check capacity before proceeding
        if method == 'dct':
            capacity = self._calculate_dct_capacity(carrier)
            if len(encrypted_data) * 8 > capacity:
                raise ValueError(f"Data too large. DCT capacity: {capacity//8} bytes")
        
        if method == 'dct':
            stego_img = self._hide_dct(encrypted_data, carrier)
        elif method == 'lsb':
            stego_img = self._hide_lsb(encrypted_data, carrier)
        else:
            raise ValueError(f"Unsupported method: {method}")
            
        # Save stego image
        cv2.imwrite(output_path, stego_img)

    def _hide_dct(self, data: bytes, carrier: np.ndarray, quality: float = 0.8) -> np.ndarray:
        """Hide data using DCT with quality control"""
        # Quality should be between 0 and 1
        quality = max(0.1, min(1.0, quality))
        
        ycrcb = cv2.cvtColor(carrier, cv2.COLOR_BGR2YCrCb)
        y = ycrcb[:,:,0]
        
        dct = fftpack.dct(fftpack.dct(y.T, norm='ortho').T, norm='ortho')
        
        # Adjust coefficient modification based on quality
        threshold = (1 - quality) * 0.1
        
        # Convert data to binary
        binary_data = ''.join(format(byte, '08b') for byte in data)
        
        # Embed data in mid-frequency coefficients
        data_index = 0
        for i in range(dct.shape[0]):
            for j in range(dct.shape[1]):
                if data_index < len(binary_data):
                    if 4 <= i + j <= 8:  # Mid-frequency band
                        dct[i,j] = np.round(dct[i,j])
                        if binary_data[data_index] == '1':
                            dct[i,j] = np.ceil(dct[i,j])
                        else:
                            dct[i,j] = np.floor(dct[i,j])
                        data_index += 1
                        
        # Inverse DCT
        y_stego = fftpack.idct(fftpack.idct(dct.T, norm='ortho').T, norm='ortho')
        ycrcb[:,:,0] = y_stego
        
        # Convert back to BGR
        stego = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
        return stego

    def _hide_lsb(self, data: bytes, carrier: np.ndarray) -> np.ndarray:
        """Hide data using LSB substitution"""
        binary_data = ''.join(format(byte, '08b') for byte in data)
        data_len = len(binary_data)
        
        # Flatten the array
        flat_carrier = carrier.flatten()
        
        if data_len > len(flat_carrier):
            raise ValueError("Data too large for carrier image")
            
        # Modify LSBs
        for i in range(data_len):
            flat_carrier[i] = (flat_carrier[i] & 254) | int(binary_data[i])
            
        return flat_carrier.reshape(carrier.shape)

    def extract_data(self, stego_image_path: str, password: str,
                    method: str = 'dct') -> bytes:
        """Extract hidden data from stego image"""
        stego = self._prepare_carrier_image(stego_image_path)
        
        if method == 'dct':
            encrypted_data = self._extract_dct(stego)
        elif method == 'lsb':
            encrypted_data = self._extract_lsb(stego)
        else:
            raise ValueError(f"Unsupported method: {method}")
            
        # Decrypt the extracted data
        decrypted_data = self._decrypt_data(encrypted_data, password)
        return self._verify_error_detection(decrypted_data)

    def _extract_dct(self, stego: np.ndarray) -> bytes:
        """Extract data from DCT coefficients"""
        # Convert to YCrCb
        ycrcb = cv2.cvtColor(stego, cv2.COLOR_BGR2YCrCb)
        y = ycrcb[:,:,0]
        
        # Apply DCT
        dct = fftpack.dct(fftpack.dct(y.T, norm='ortho').T, norm='ortho')
        
        # Extract bits from coefficients
        extracted_bits = []
        for i in range(dct.shape[0]):
            for j in range(dct.shape[1]):
                if 4 <= i + j <= 8:
                    bit = '1' if np.round(dct[i,j]) % 2 == 1 else '0'
                    extracted_bits.append(bit)
                    
        # Convert bits to bytes
        extracted_bytes = []
        for i in range(0, len(extracted_bits), 8):
            byte = int(''.join(extracted_bits[i:i+8]), 2)
            extracted_bytes.append(byte)
            
        return bytes(extracted_bytes)

    def _extract_lsb(self, stego: np.ndarray) -> bytes:
        """Extract data from LSBs"""
        # Get LSBs
        flat_stego = stego.flatten()
        extracted_bits = [str(pixel & 1) for pixel in flat_stego]
        
        # Convert bits to bytes
        extracted_bytes = []
        for i in range(0, len(extracted_bits), 8):
            byte = int(''.join(extracted_bits[i:i+8]), 2)
            extracted_bytes.append(byte)
            
        return bytes(extracted_bytes) 