import tkinter as tk
from tkinter import ttk, filedialog
from typing import Optional, Callable
from pathlib import Path

class FileSelector(ttk.Frame):
    def __init__(self, parent, label: str, file_types: list, 
                 on_select: Optional[Callable] = None):
        super().__init__(parent)
        self.file_types = file_types
        self.on_select = on_select
        self.selected_path = None
        
        # Create widgets
        self.label = ttk.Label(self, text=label)
        self.path_var = tk.StringVar()
        self.path_entry = ttk.Entry(self, textvariable=self.path_var, width=40)
        self.browse_btn = ttk.Button(self, text="Browse", command=self._browse)
        
        # Layout
        self.label.pack(side=tk.LEFT, padx=5)
        self.path_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.browse_btn.pack(side=tk.LEFT, padx=5)
        
    def _browse(self) -> None:
        """Open file dialog and handle selection"""
        path = filedialog.askopenfilename(filetypes=self.file_types)
        if path:
            self.selected_path = Path(path)
            self.path_var.set(str(self.selected_path))
            if self.on_select:
                self.on_select(self.selected_path)
                
    def get_path(self) -> Optional[Path]:
        """Get selected file path"""
        return self.selected_path
        
    def clear(self) -> None:
        """Clear selection"""
        self.selected_path = None
        self.path_var.set("") 