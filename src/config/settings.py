from typing import Dict, Any
import json
import os

DEFAULT_SETTINGS = {
    "theme": "Light",
    "max_file_size_mb": 10,
    "default_method": "dct",
    "default_quality": 0.8,
    "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
    "encryption": {
        "iterations": 200000,
        "key_length": 32
    }
}

class Settings:
    def __init__(self, settings_file: str = "stego_settings.json"):
        self.settings_file = settings_file
        self.settings = self.load()
        
    def load(self) -> Dict[str, Any]:
        """Load settings from file or return defaults"""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                return {**DEFAULT_SETTINGS, **json.load(f)}
        return DEFAULT_SETTINGS.copy()
        
    def save(self) -> None:
        """Save current settings to file"""
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f, indent=4)
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save() 