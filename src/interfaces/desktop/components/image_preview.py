import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from typing import Optional, Tuple
from pathlib import Path

class ImagePreview(ttk.Frame):
    def __init__(self, parent, max_size: Tuple[int, int] = (400, 300)):
        super().__init__(parent)
        self.max_size = max_size
        
        # Create canvas for image
        self.canvas = tk.Canvas(self, width=max_size[0], height=max_size[1])
        self.canvas.pack(expand=True, fill=tk.BOTH)
        
        # Info labels
        self.info_frame = ttk.Frame(self)
        self.size_label = ttk.Label(self.info_frame, text="Size: ")
        self.format_label = ttk.Label(self.info_frame, text="Format: ")
        
        self.size_label.pack(side=tk.LEFT, padx=5)
        self.format_label.pack(side=tk.LEFT, padx=5)
        self.info_frame.pack(fill=tk.X)
        
        self.current_image = None
        
    def show(self, image_path: Path) -> None:
        """Display image with size constraints"""
        try:
            image = Image.open(image_path)
            
            # Calculate resize ratio
            ratio = min(self.max_size[0]/image.width, 
                       self.max_size[1]/image.height)
            new_size = (int(image.width * ratio), 
                       int(image.height * ratio))
            
            # Resize and convert for display
            image = image.resize(new_size, Image.Resampling.LANCZOS)
            self.current_image = ImageTk.PhotoImage(image)
            
            # Update canvas
            self.canvas.delete("all")
            self.canvas.create_image(
                self.max_size[0]//2, 
                self.max_size[1]//2,
                image=self.current_image,
                anchor=tk.CENTER
            )
            
            # Update info
            self.size_label.config(text=f"Size: {image.width}x{image.height}")
            self.format_label.config(text=f"Format: {image.format}")
            
        except Exception as e:
            self.clear()
            raise ValueError(f"Error loading image: {str(e)}")
            
    def clear(self) -> None:
        """Clear current image"""
        self.canvas.delete("all")
        self.current_image = None
        self.size_label.config(text="Size: ")
        self.format_label.config(text="Format: ") 