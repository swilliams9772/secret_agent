import unittest
import os
import numpy as np
from src.steganography import SteganoExfil

class TestSteganography(unittest.TestCase):
    def setUp(self):
        self.stego = SteganoExfil()
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_data_dir = os.path.join(self.test_dir, 'test_data')
        self.carrier_path = os.path.join(self.test_data_dir, 'test_carrier.png')
        self.secret_path = os.path.join(self.test_data_dir, 'test_secret.txt')
        self.output_path = os.path.join(self.test_data_dir, 'test_output.png')
        self.password = "test_password"

    def tearDown(self):
        # Clean up any test files
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_dct_hide_extract(self):
        """Test DCT method hide and extract"""
        with open(self.secret_path, 'rb') as f:
            original_data = f.read()

        # Hide data
        self.stego.hide_data(
            data=original_data,
            carrier_image_path=self.carrier_path,
            output_path=self.output_path,
            password=self.password,
            method='dct'
        )

        # Extract data
        extracted_data = self.stego.extract_data(
            stego_image_path=self.output_path,
            password=self.password,
            method='dct'
        )

        self.assertEqual(original_data, extracted_data)

    def test_lsb_hide_extract(self):
        """Test LSB method hide and extract"""
        with open(self.secret_path, 'rb') as f:
            original_data = f.read()

        # Hide data
        self.stego.hide_data(
            data=original_data,
            carrier_image_path=self.carrier_path,
            output_path=self.output_path,
            password=self.password,
            method='lsb'
        )

        # Extract data
        extracted_data = self.stego.extract_data(
            stego_image_path=self.output_path,
            password=self.password,
            method='lsb'
        )

        self.assertEqual(original_data, extracted_data)

    def test_capacity_validation(self):
        """Test capacity validation"""
        # Create data larger than carrier capacity
        large_data = os.urandom(1024 * 1024)  # 1MB of random data

        with self.assertRaises(ValueError):
            self.stego.hide_data(
                data=large_data,
                carrier_image_path=self.carrier_path,
                output_path=self.output_path,
                password=self.password,
                method='dct'
            )

if __name__ == '__main__':
    unittest.main() 