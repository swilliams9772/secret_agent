import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Dict

class MethodSelector(ttk.LabelFrame):
    def __init__(self, parent, on_change: Optional[Callable] = None):
        super().__init__(parent, text="Steganography Method")
        self.on_change = on_change
        
        # Method information
        self.method_info: Dict[str, Dict] = {
            'dct': {
                'name': 'Discrete Cosine Transform',
                'security': 'High',
                'capacity': 'Medium',
                'speed': 'Medium'
            },
            'lsb': {
                'name': 'Least Significant Bit',
                'security': 'Medium',
                'capacity': 'High',
                'speed': 'High'
            }
        }
        
        self._create_widgets()
        self._create_layout()
        
    def _create_widgets(self):
        """Create method selection widgets"""
        # Method selection
        self.method_var = tk.StringVar(value='dct')
        self.method_frame = ttk.Frame(self)
        
        # Radio buttons
        self.dct_radio = ttk.Radiobutton(
            self.method_frame,
            text="DCT",
            variable=self.method_var,
            value='dct',
            command=self._on_method_change
        )
        
        self.lsb_radio = ttk.Radiobutton(
            self.method_frame,
            text="LSB",
            variable=self.method_var,
            value='lsb',
            command=self._on_method_change
        )
        
        # Info display
        self.info_frame = ttk.Frame(self)
        self.security_label = ttk.Label(self.info_frame, text="Security: ")
        self.capacity_label = ttk.Label(self.info_frame, text="Capacity: ")
        self.speed_label = ttk.Label(self.info_frame, text="Speed: ")
        
    def _create_layout(self):
        """Create widget layout"""
        self.method_frame.pack(fill=tk.X, padx=5, pady=5)
        self.dct_radio.pack(side=tk.LEFT, padx=5)
        self.lsb_radio.pack(side=tk.LEFT, padx=5)
        
        self.info_frame.pack(fill=tk.X, padx=5, pady=5)
        self.security_label.pack(fill=tk.X, padx=5)
        self.capacity_label.pack(fill=tk.X, padx=5)
        self.speed_label.pack(fill=tk.X, padx=5)
        
        self._update_info()
        
    def _on_method_change(self):
        """Handle method change"""
        self._update_info()
        if self.on_change:
            self.on_change(self.method_var.get())
            
    def _update_info(self):
        """Update method information display"""
        method = self.method_var.get()
        info = self.method_info[method]
        
        self.security_label.config(text=f"Security: {info['security']}")
        self.capacity_label.config(text=f"Capacity: {info['capacity']}")
        self.speed_label.config(text=f"Speed: {info['speed']}")
        
    def get_method(self) -> str:
        """Get selected method"""
        return self.method_var.get() 