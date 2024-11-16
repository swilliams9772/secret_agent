from typing import Dict, Any, Optional
import json
import os
from pathlib import Path

class Settings:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.settings: Dict[str, Any] = self._load_defaults()
        self.load()
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        """Load settings from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.settings.update(loaded)
        except Exception as e:
            print(f"Error loading settings: {e}")
            
    def save(self) -> None:
        """Save current settings to file"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
        
    def set(self, key: str, value: Any) -> None:
        """Set setting value and save"""
        self.settings[key] = value
        self.save()
        
    def add_recent_file(self, filepath: str) -> None:
        """Add file to recent files list"""
        recent = self.get("recent_files", [])
        if filepath in recent:
            recent.remove(filepath)
        recent.insert(0, filepath)
        recent = recent[:self.get("max_recent_files", 5)]
        self.set("recent_files", recent)
        
    def _load_defaults(self) -> Dict[str, Any]:
        """Load default settings"""
        return {
            "theme": "Light",
            "max_file_size_mb": 10,
            "default_method": "dct",
            "default_quality": 0.8,
            "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
            "temp_dir": "temp",
            "recent_files": [],
            "auto_cleanup": True,
            "preview_size": (300, 300),
            "max_recent_files": 5
        }
        
    def load(self) -> None:
        self.save() 