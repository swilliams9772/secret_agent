import streamlit as st
import json
from pathlib import Path
from typing import Dict, Any, Optional

class SettingsPanel:
    def __init__(self, settings_path: Optional[Path] = None):
        self.settings_path = settings_path or Path("config/settings.json")
        self.settings = self.load_settings()
        
    def load_settings(self) -> Dict[str, Any]:
        """Load settings from JSON file"""
        try:
            if self.settings_path.exists():
                return json.loads(self.settings_path.read_text())
        except Exception as e:
            st.error(f"Error loading settings: {str(e)}")
            
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "auto_cleanup": True,
            "preview_size": [300, 300],
            "compression_level": 0
        }
        
    def render(self) -> Dict[str, Any]:
        """Render settings panel and return updated settings"""
        st.subheader("⚙️ Settings")
        
        with st.expander("General Settings"):
            self.settings["theme"] = st.selectbox(
                "Theme",
                options=["Light", "Dark", "Custom"],
                index=["Light", "Dark", "Custom"].index(self.settings["theme"])
            )
            
            self.settings["max_file_size_mb"] = st.number_input(
                "Maximum File Size (MB)",
                min_value=1,
                max_value=100,
                value=self.settings["max_file_size_mb"]
            )
            
            self.settings["auto_cleanup"] = st.checkbox(
                "Auto Cleanup Temporary Files",
                value=self.settings["auto_cleanup"]
            )
        
        with st.expander("Steganography Settings"):
            self.settings["default_method"] = st.selectbox(
                "Default Method",
                options=["dct", "lsb"],
                index=["dct", "lsb"].index(self.settings["default_method"])
            )
            
            self.settings["default_quality"] = st.slider(
                "Default Quality",
                min_value=0.1,
                max_value=1.0,
                value=float(self.settings["default_quality"]),
                step=0.1
            )
            
            self.settings["compression_level"] = st.slider(
                "Compression Level",
                min_value=0,
                max_value=9,
                value=self.settings["compression_level"]
            )
        
        if st.button("Save Settings"):
            self.save_settings()
            st.success("Settings saved successfully!")
            
        return self.settings
    
    def save_settings(self) -> None:
        """Save settings to JSON file"""
        try:
            self.settings_path.parent.mkdir(parents=True, exist_ok=True)
            self.settings_path.write_text(json.dumps(self.settings, indent=4))
        except Exception as e:
            st.error(f"Error saving settings: {str(e)}") 