import tkinter as tk
from tkinter import ttk
from typing import Optional
from datetime import datetime

class StatusBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Create widgets
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            self, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            padding=(5, 2)
        )
        
        self.time_var = tk.StringVar()
        self.time_label = ttk.Label(
            self,
            textvariable=self.time_var,
            relief=tk.SUNKEN,
            padding=(5, 2)
        )
        
        # Layout
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.time_label.pack(side=tk.RIGHT, padx=5)
        
        self._update_time()
        
    def set_status(self, message: str, level: Optional[str] = None) -> None:
        """Update status message with optional level"""
        self.status_var.set(message)
        
        if level == "error":
            self.status_label.configure(foreground="red")
        elif level == "success":
            self.status_label.configure(foreground="green")
        elif level == "warning":
            self.status_label.configure(foreground="orange")
        else:
            self.status_label.configure(foreground="black")
            
    def _update_time(self) -> None:
        """Update time display"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_var.set(current_time)
        self.after(1000, self._update_time) 