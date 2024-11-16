import streamlit as st
from pathlib import Path
from typing import Optional, Tuple, Union
import mimetypes

class FileUploader:
    def __init__(self, key_prefix: str, max_size_mb: int = 10):
        self.key_prefix = key_prefix
        self.max_size_mb = max_size_mb
        self.supported_image_types = {'.png', '.jpg', '.jpeg', '.bmp'}
        
    def upload_carrier(self) -> Optional[Tuple[bytes, Path]]:
        """Upload carrier image with validation"""
        uploaded_file = st.file_uploader(
            "Choose carrier image",
            type=list(self.supported_image_types),
            key=f"{self.key_prefix}_carrier"
        )
        
        if uploaded_file:
            if self._validate_file_size(uploaded_file):
                return uploaded_file.getvalue(), Path(uploaded_file.name)
            else:
                st.error(f"File too large (max {self.max_size_mb}MB)")
        return None
        
    def upload_data(self) -> Optional[Tuple[bytes, str]]:
        """Upload data file with size validation"""
        uploaded_file = st.file_uploader(
            "Choose data file",
            key=f"{self.key_prefix}_data"
        )
        
        if uploaded_file:
            if self._validate_file_size(uploaded_file):
                mime_type = mimetypes.guess_type(uploaded_file.name)[0] or 'application/octet-stream'
                return uploaded_file.getvalue(), mime_type
            else:
                st.error(f"File too large (max {self.max_size_mb}MB)")
        return None
        
    def _validate_file_size(self, file) -> bool:
        """Validate file size against maximum limit"""
        return file.size <= self.max_size_mb * 1024 * 1024 