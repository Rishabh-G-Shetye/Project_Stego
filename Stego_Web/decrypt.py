import sys
from PIL import Image

def decrypt_message(image_path):
    img = Image.open(image_path).convert('RGBA')
    data = list(img.getdata())

    binary_message = ""
    for pixel in data:
        r, g, b, a = pixel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            message += char
            if message.endswith("####END####"):
                if len(message) > 10:
                    return message[:-11]
                else:
                    return ""
        else:
            break
    return "No hidden message found."

if __name__ == "__main__":
    image_path = sys.argv[1]
    decrypted_message = decrypt_message(image_path)
    print(decrypted_message)