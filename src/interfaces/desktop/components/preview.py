import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class ImagePreview(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.preview_size = (300, 300)
        self._setup_ui()
        
    def _setup_ui(self):
        """Setup the preview frame UI"""
        self.preview_label = ttk.Label(self)
        self.preview_label.pack(expand=True, fill=tk.BOTH)
        
    def update_preview(self, image_path: str) -> None:
        """Update the preview with a new image"""
        try:
            if not os.path.exists(image_path):
                self.clear_preview()
                return
                
            image = Image.open(image_path)
            image.thumbnail(self.preview_size)
            photo = ImageTk.PhotoImage(image)
            
            self.preview_label.configure(image=photo)
            self.preview_label.image = photo  # Keep reference
            
        except Exception as e:
            self.clear_preview()
            raise ValueError(f"Failed to load preview: {str(e)}")
            
    def clear_preview(self) -> None:
        """Clear the current preview"""
        self.preview_label.configure(image='')
        self.preview_label.image = None 