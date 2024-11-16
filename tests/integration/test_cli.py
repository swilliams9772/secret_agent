import pytest
from pathlib import Path
from steganography.cli import CLI
import numpy as np
import cv2

@pytest.fixture
def cli():
    return CLI()

@pytest.fixture
def test_files(tmp_path):
    """Create test files"""
    # Create carrier image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    carrier_path = tmp_path / "carrier.png"
    cv2.imwrite(str(carrier_path), img)
    
    # Create data file
    data_path = tmp_path / "secret.txt"
    data_path.write_text("Secret test data")
    
    return {
        "carrier": carrier_path,
        "data": data_path,
        "output": tmp_path / "stego.png",
        "extracted": tmp_path / "extracted.txt"
    }

class TestCLI:
    def test_hide_command(self, cli, test_files):
        """Test hide command"""
        args = [
            "hide",
            "-i", str(test_files["carrier"]),
            "-d", str(test_files["data"]),
            "-o", str(test_files["output"]),
            "-p", "test123",
            "-m", "dct"
        ]
        
        exit_code = cli.run(args)
        assert exit_code == 0
        assert test_files["output"].exists()

    def test_extract_command(self, cli, test_files):
        """Test extract command"""
        # First hide data
        hide_args = [
            "hide",
            "-i", str(test_files["carrier"]),
            "-d", str(test_files["data"]),
            "-o", str(test_files["output"]),
            "-p", "test123",
            "-m", "dct"
        ]
        cli.run(hide_args)
        
        # Then extract
        extract_args = [
            "extract",
            "-i", str(test_files["output"]),
            "-o", str(test_files["extracted"]),
            "-p", "test123",
            "-m", "dct"
        ]
        exit_code = cli.run(extract_args)
        
        assert exit_code == 0
        assert test_files["extracted"].exists()
        assert test_files["extracted"].read_text() == test_files["data"].read_text()

    def test_invalid_arguments(self, cli):
        """Test CLI with invalid arguments"""
        args = ["hide", "-i", "nonexistent.png"]
        exit_code = cli.run(args)
        assert exit_code != 0 