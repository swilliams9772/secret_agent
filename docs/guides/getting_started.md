# Getting Started

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install package
pip install -r requirements.txt
```

## Basic Usage

### Command Line
```bash
# Hide data
stego-cli hide -i input.png -o output.png -p password -m dct

# Extract data
stego-cli extract -i stego.png -o extracted -p password -m dct
```

### Python API
```python
from steganography import SteganoExfil

# Initialize
stego = SteganoExfil()

# Hide data
stego.hide_data(
    data=secret_data,
    carrier_image_path='input.png',
    output_path='output.png',
    password='password',
    method='dct'
)

# Extract data
data = stego.extract_data(
    stego_image_path='output.png',
    password='password',
    method='dct'
)
```

### Web Interface
```bash
streamlit run src/streamlit_app.py
```

### Desktop GUI
```bash
python src/stego_gui.py
``` 