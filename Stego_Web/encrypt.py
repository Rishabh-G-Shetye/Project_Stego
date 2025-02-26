import sys
from PIL import Image

def encrypt_message(image_path, message):
    img = Image.open(image_path).convert('RGBA')
    width, height = img.size
    data = list(img.getdata())

    message += "####END####"
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '0' * (8 - len(binary_message) % 8) if len(binary_message) % 8 != 0 else '' #pad to byte boundary

    if len(binary_message) > width * height * 3:
        raise ValueError("Message too large to fit in image.")

    binary_index = 0
    new_data = []

    for pixel in data:
        r, g, b, a = pixel
        if binary_index < len(binary_message):
            r = (r & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            g = (g & ~1) | int(binary_message[binary_index])
            binary_index += 1
        if binary_index < len(binary_message):
            b = (b & ~1) | int(binary_message[binary_index])
            binary_index += 1
        new_data.append((r, g, b, a))

    img.putdata(new_data)
    img.save("encrypted_image.png")

if __name__ == "__main__":
    image_path = sys.argv[1]
    message = sys.argv[2]
    encrypt_message(image_path, message)