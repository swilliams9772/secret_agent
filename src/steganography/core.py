import numpy as np
import cv2
from scipy import fftpack
import os

from .encryption import encrypt_data, decrypt_data
from .utils import add_error_detection, verify_error_detection, encode_data_length, decode_data_length
from .exceptions import SteganoError, CapacityError, FormatError

class SteganoExfil:
    def __init__(self):
        self.supported_formats = ['.png', '.jpg', '.jpeg', '.bmp']
        self.quality = 0.8
        
    def _prepare_carrier_image(self, image_path: str) -> np.ndarray:
        """Load and prepare carrier image with format handling"""
        ext = os.path.splitext(image_path)[1].lower()
        if ext not in self.supported_formats:
            raise FormatError(f"Unsupported format: {ext}")
        
        if ext in ['.jpg', '.jpeg']:
            img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
            if img is None:
                raise FormatError("Could not load image")
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

    def hide_data(self, data: bytes, carrier_image_path: str, 
                 output_path: str, password: str,
                 method: str = 'dct', quality: float = None) -> None:
        """Hide data in carrier image using specified method"""
        if quality is not None:
            self.quality = max(0.1, min(1.0, quality))
            
        # Add error detection and length prefix
        data_with_detection = add_error_detection(data)
        data_with_length = encode_data_length(len(data_with_detection)) + data_with_detection
        encrypted_data = encrypt_data(data_with_length, password)
        
        # Load and validate carrier
        carrier = self._prepare_carrier_image(carrier_image_path)
        
        # Check capacity
        if method == 'dct':
            capacity = self._calculate_dct_capacity(carrier)
            if len(encrypted_data) * 8 > capacity:
                raise CapacityError("Data too large for carrier using DCT method")
            stego_img = self._hide_dct(encrypted_data, carrier)
        elif method == 'lsb':
            if len(encrypted_data) * 8 > carrier.size * 3:
                raise CapacityError("Data too large for carrier using LSB method")
            stego_img = self._hide_lsb(encrypted_data, carrier)
        else:
            raise ValueError(f"Unsupported method: {method}")
            
        # Save stego image
        cv2.imwrite(output_path, stego_img)

    def _hide_dct(self, data: bytes, carrier: np.ndarray) -> np.ndarray:
        """Hide data using DCT with quality control"""
        ycrcb = cv2.cvtColor(carrier, cv2.COLOR_BGR2YCrCb)
        y = ycrcb[:,:,0]
        
        dct = fftpack.dct(fftpack.dct(y.T, norm='ortho').T, norm='ortho')
        
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
        
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

    def _hide_lsb(self, data: bytes, carrier: np.ndarray) -> np.ndarray:
        """Hide data using LSB substitution"""
        binary_data = ''.join(format(byte, '08b') for byte in data)
        data_len = len(binary_data)
        
        flat_carrier = carrier.flatten()
        if data_len > len(flat_carrier):
            raise CapacityError("Data too large for carrier image")
            
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
            
        # Decrypt and verify data
        decrypted_data = decrypt_data(encrypted_data, password)
        length = decode_data_length(decrypted_data[:4])
        data_with_detection = decrypted_data[4:4+length]
        return verify_error_detection(data_with_detection)

    def _extract_dct(self, stego: np.ndarray) -> bytes:
        """Extract data from DCT coefficients"""
        ycrcb = cv2.cvtColor(stego, cv2.COLOR_BGR2YCrCb)
        y = ycrcb[:,:,0]
        
        dct = fftpack.dct(fftpack.dct(y.T, norm='ortho').T, norm='ortho')
        
        extracted_bits = []
        for i in range(dct.shape[0]):
            for j in range(dct.shape[1]):
                if 4 <= i + j <= 8:
                    bit = '1' if np.round(dct[i,j]) % 2 == 1 else '0'
                    extracted_bits.append(bit)
                    
        extracted_bytes = []
        for i in range(0, len(extracted_bits), 8):
            byte = int(''.join(extracted_bits[i:i+8]), 2)
            extracted_bytes.append(byte)
            
        return bytes(extracted_bytes)

    def _extract_lsb(self, stego: np.ndarray) -> bytes:
        """Extract data from LSBs"""
        flat_stego = stego.flatten()
        extracted_bits = [str(pixel & 1) for pixel in flat_stego]
        
        extracted_bytes = []
        for i in range(0, len(extracted_bits), 8):
            byte = int(''.join(extracted_bits[i:i+8]), 2)
            extracted_bytes.append(byte)
            
        return bytes(extracted_bytes) 