import pytest
import numpy as np
import cv2
from pathlib import Path
from steganography import SteganoExfil
from steganography.exceptions import CapacityError, FormatError

@pytest.fixture
def stego():
    return SteganoExfil()

@pytest.fixture
def test_data():
    return b"Hello, World! This is test data."

@pytest.fixture
def carrier_image():
    # Create a test image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img_path = Path("tests/data/test_carrier.png")
    img_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(img_path), img)
    return str(img_path)

class TestSteganoExfil:
    def test_dct_hide_extract(self, stego, test_data, carrier_image, tmp_path):
        """Test DCT method hide and extract cycle"""
        output_path = tmp_path / "stego.png"
        password = "test123"

        # Hide data
        stego.hide_data(
            data=test_data,
            carrier_image_path=carrier_image,
            output_path=str(output_path),
            password=password,
            method='dct'
        )

        # Extract data
        extracted = stego.extract_data(
            stego_image_path=str(output_path),
            password=password,
            method='dct'
        )

        assert extracted == test_data

    def test_lsb_hide_extract(self, stego, test_data, carrier_image, tmp_path):
        """Test LSB method hide and extract cycle"""
        output_path = tmp_path / "stego.png"
        password = "test123"

        # Hide data
        stego.hide_data(
            data=test_data,
            carrier_image_path=carrier_image,
            output_path=str(output_path),
            password=password,
            method='lsb'
        )

        # Extract data
        extracted = stego.extract_data(
            stego_image_path=str(output_path),
            password=password,
            method='lsb'
        )

        assert extracted == test_data

    def test_capacity_validation(self, stego, carrier_image, tmp_path):
        """Test capacity validation"""
        large_data = b"x" * (1024 * 1024)  # 1MB
        output_path = tmp_path / "stego.png"
        password = "test123"

        with pytest.raises(CapacityError):
            stego.hide_data(
                data=large_data,
                carrier_image_path=carrier_image,
                output_path=str(output_path),
                password=password,
                method='dct'
            )

    def test_invalid_format(self, stego, test_data, tmp_path):
        """Test invalid format handling"""
        invalid_path = tmp_path / "test.txt"
        invalid_path.write_text("not an image")
        output_path = tmp_path / "stego.png"
        password = "test123"

        with pytest.raises(FormatError):
            stego.hide_data(
                data=test_data,
                carrier_image_path=str(invalid_path),
                output_path=str(output_path),
                password=password
            ) 