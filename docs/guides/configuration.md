# Configuration Guide

## Settings File
Location: `stego_settings.json`

```json
{
    "theme": "Light",
    "max_file_size_mb": 10,
    "default_method": "dct",
    "default_quality": 0.8,
    "supported_formats": [".png", ".jpg", ".jpeg", ".bmp"],
    "temp_dir": "temp",
    "recent_files": [],
    "auto_cleanup": true,
    "preview_size": [300, 300],
    "max_recent_files": 5
}
```

## Quality Settings

| Quality | Capacity | Security | Use Case |
|---------|----------|-----------|-----------|
| 0.9-1.0 | Low | Best | Sensitive data |
| 0.5-0.8 | Medium | Good | General use |
| 0.1-0.4 | High | Basic | Large files |

## Format Support

### Image Formats
- PNG (Recommended)
- JPEG (Limited)
- BMP (Supported)

### Data Formats
- Any binary data
- Text files
- Images
- Documents 