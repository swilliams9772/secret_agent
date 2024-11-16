# Advanced Usage Guide

## Steganography Methods

### DCT (Discrete Cosine Transform)
- More secure, resistant to statistical analysis
- Better image quality preservation
- Lower capacity (~1-5% of image size)
- Suitable for sensitive data

Example:
```python
stego.hide_data(
    data=secret_data,
    carrier_image_path='input.png',
    output_path='output.png',
    password='password',
    method='dct',
    quality=0.9  # Higher quality = better security
)
```

### LSB (Least Significant Bit)
- Higher capacity (up to 12.5% of image size)
- Faster processing
- Less secure against statistical analysis
- Best for large files

Example:
```python
stego.hide_data(
    data=large_data,
    carrier_image_path='input.png',
    output_path='output.png',
    password='password',
    method='lsb'
)
```

## Security Considerations

### Password Guidelines
- Use strong, unique passwords
- Minimum 12 characters recommended
- Mix of character types
- Avoid common phrases

### File Handling
- Use fresh carrier images
- Avoid reusing stego images
- Clear temporary files
- Verify extracted data integrity

### Operational Security
- Process data locally
- Use secure channels
- Monitor file sizes
- Check image metadata 