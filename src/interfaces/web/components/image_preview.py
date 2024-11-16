import streamlit as st
from PIL import Image
import io
from typing import Optional
import numpy as np

class ImagePreview:
    def __init__(self, max_width: int = 400):
        self.max_width = max_width
        
    def show(self, image_data: bytes, caption: Optional[str] = None) -> None:
        """Display image preview with optional caption"""
        try:
            image = Image.open(io.BytesIO(image_data))
            
            # Resize if needed
            if image.width > self.max_width:
                ratio = self.max_width / image.width
                new_size = (self.max_width, int(image.height * ratio))
                image = image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Display image
            st.image(image, caption=caption, use_column_width=True)
            
            # Show image info
            with st.expander("Image Information"):
                st.write(f"Format: {image.format}")
                st.write(f"Size: {image.size}")
                st.write(f"Mode: {image.mode}")
                
        except Exception as e:
            st.error(f"Error displaying image: {str(e)}") 