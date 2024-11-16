from steganography import SteganoExfil

# Initialize
stego = SteganoExfil()

# Hide data
with open('secret.txt', 'rb') as f:
    secret_data = f.read()
    
stego.hide_data(
    data=secret_data,
    carrier_image_path='cover.png',
    output_path='stego.png',
    password='MySecretPass123',
    method='dct',
    quality=0.9  # Higher quality, less capacity
)

# Extract data
extracted_data = stego.extract_data(
    stego_image_path='stego.png',
    password='MySecretPass123',
    method='dct'
)

# Save extracted data
with open('extracted.txt', 'wb') as f:
    f.write(extracted_data) 