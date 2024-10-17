from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, shift_value):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB format
    pixels = img.load()
    
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply shift (encryption) with modulo 256 to ensure the pixel values stay within the range
            encrypted_r = (r + shift_value) % 256
            encrypted_g = (g + shift_value) % 256
            encrypted_b = (b + shift_value) % 256

            pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)
    
    return img

# Function to decrypt the image
def decrypt_image(encrypted_image_path, shift_value):
    img = Image.open(encrypted_image_path)
    img = img.convert("RGB")
    pixels = img.load()
    
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Apply reverse shift (decryption) with modulo 256
            decrypted_r = (r - shift_value) % 256
            decrypted_g = (g - shift_value) % 256
            decrypted_b = (b - shift_value) % 256

            pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)
    
    return img

if __name__ == "__main__":
    input_image_path = 'input_image.png'  # Ensure this image exists (use a PNG for lossless encryption)
    encrypted_image_path = 'encrypted_image.png'
    decrypted_image_path = 'decrypted_image.png'
    shift_value = 50  # Any shift value of your choice

    # Encrypt the image
    encrypted_image = encrypt_image(input_image_path, shift_value)
    encrypted_image.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image_path, shift_value)
    decrypted_image.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")
