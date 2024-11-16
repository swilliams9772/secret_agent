import tkinter as tk
from tkinter import ttk
from typing import Optional

class ProgressBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create widgets
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            self,
            variable=self.progress_var,
            maximum=100,
            mode='determinate'
        )
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(self, textvariable=self.status_var)
        
        # Layout
        self.progress.pack(fill=tk.X, padx=5, pady=2)
        self.status_label.pack(fill=tk.X, padx=5)
        
    def start(self, message: str = "Processing...") -> None:
        """Start progress indication"""
        self.progress_var.set(0)
        self.status_var.set(message)
        self.update()
        
    def update(self, value: float = 0, message: Optional[str] = None) -> None:
        """Update progress value and message"""
        self.progress_var.set(value * 100)
        if message:
            self.status_var.set(message)
        self.update_idletasks()
        
    def complete(self, message: str = "Complete!", success: bool = True) -> None:
        """Complete progress with success/error indication"""
        self.progress_var.set(100)
        self.status_var.set(message)
        if not success:
            self.progress.configure(style='Error.Horizontal.TProgressbar')
        self.update_idletasks() 