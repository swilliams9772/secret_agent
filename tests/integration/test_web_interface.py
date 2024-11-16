import pytest
from streamlit.testing.v1 import AppTest
from pathlib import Path
import numpy as np
import cv2

@pytest.fixture
def app():
    return AppTest.from_file("src/interfaces/web/app.py")

@pytest.fixture
def test_image():
    """Create a test image"""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img_path = Path("tests/data/test_carrier.png")
    img_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(img_path), img)
    return img_path

class TestWebInterface:
    def test_app_loads(self, app):
        """Test that app loads successfully"""
        app.run()
        assert app.title == "🕵️‍♂️ Steganography Tool"

    def test_file_upload(self, app, test_image):
        """Test file upload functionality"""
        app.run()
        
        # Upload carrier image
        with open(test_image, "rb") as f:
            app.file_uploader(key="hide_carrier").upload(f)
            
        # Check that image preview is shown
        assert len(app.image) > 0

    def test_settings_persistence(self, app):
        """Test settings save and load"""
        app.run()
        
        # Change settings
        app.slider("Default image quality").set_value(0.5)
        app.button("Save Settings").click()
        
        # Reload app
        app.rerun()
        
        # Check settings persisted
        assert app.slider("Default image quality").value == 0.5

    def test_error_handling(self, app, test_image):
        """Test error handling for invalid operations"""
        app.run()
        
        # Try to hide without password
        with open(test_image, "rb") as f:
            app.file_uploader(key="hide_carrier").upload(f)
            
        app.button("Hide Data").click()
        
        # Should show error
        assert "Error" in app.error[0] 