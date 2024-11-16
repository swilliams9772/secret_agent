import streamlit as st
from typing import Optional
import time

class ProgressBar:
    def __init__(self):
        self.progress = None
        
    def start(self, message: str = "Processing...") -> None:
        """Start progress bar with message"""
        self.progress = st.progress(0)
        self.status = st.empty()
        self.status.text(message)
        
    def update(self, value: float, message: Optional[str] = None) -> None:
        """Update progress bar value and message"""
        if self.progress is not None:
            self.progress.progress(value)
            if message:
                self.status.text(message)
                
    def complete(self, message: str = "Complete!", success: bool = True) -> None:
        """Complete progress bar with success/error message"""
        if self.progress is not None:
            self.progress.progress(1.0)
            if success:
                self.status.success(message)
            else:
                self.status.error(message)
            time.sleep(0.5)  # Brief pause to show completion
            self.progress.empty()
            self.progress = None 