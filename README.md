# Secure Data Hiding in Images Using Steganography

This project provides a simple and secure web application for hiding text messages within images using steganography. It utilizes the Least Significant Bit (LSB) method for embedding data and prioritizes local processing to enhance user privacy.

## Problem Statement

The need for secure and discreet data transfer is paramount in today's digital landscape. This web application addresses the challenge of hiding sensitive textual information within images, providing a user-friendly platform for steganographic encryption and decryption. Users require a simple, intuitive interface to seamlessly embed and retrieve secret messages, ensuring data confidentiality through password-protected access. Furthermore, the application aims to minimize the risk of data detection by utilizing a refined Least Significant Bit (LSB) algorithm, while also offering a local processing environment to enhance user privacy and control over their data.

## Features

* **Local Processing:** All encryption and decryption are performed locally on the user's computer, ensuring data privacy.
* **User-Friendly Interface:** Simple and intuitive web interface for easy use.
* **Password Protection:** Secure data hiding with password-protected encryption and decryption.
* **Direct File Download:** Download encrypted images directly to your device.
* **LSB Steganography:** Implements a refined Least Significant Bit algorithm for data hiding.
* **Self-Contained:** All required files are included, making it easy to set up and run.

## Technologies Used

* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript
* **Backend:**
    * PHP
    * XAMPP (Apache, MySQL, PHP)
* **Steganography Processing:**
    * Python
    * PIL (Pillow)

## Installation

1.  **Install XAMPP:** Download and install XAMPP from [apachefriends.org](https://www.apachefriends.org/).
2.  **Start Apache:** Start the Apache service from the XAMPP Control Panel.
3.  **Clone or Download the Repository:** Clone or download this repository to your XAMPP `htdocs` directory (e.g., `C:\xampp\htdocs\`).
4.  **Install Python Libraries:** Open your command prompt or terminal and run:
    ```bash
    pip install Pillow
    ```
5.  **Open in Browser:** Open your web browser and navigate to `http://localhost/Stego_Web/index.php`.

## Usage

1.  **Encrypting an Image:**
    * Select an image file to encrypt.
    * Enter the secret message you want to hide.
    * Enter a password for encryption.
    * Click the "Encrypt" button.
    * Download the encrypted image.

2.  **Decrypting an Image:**
    * Select the encrypted image file.
    * Enter the password used for encryption.
    * Click the "Decrypt" button.
    * The decrypted message will be displayed.

## Wow Factors

| Feature                     | Benefit                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| **Local Processing** | Enhanced user privacy; data remains on user's device.              |
| **Simple Interface** | Accessible to all users, regardless of technical expertise.           |
| **Direct File Download** | Seamless download of encrypted images; no external plugins needed.        |
| **Self-Contained Solution** | Complete, downloadable package; minimal dependencies.                |
| **Educational Value** | Demonstrates steganography principles; useful for learning.         |

## Conclusion

This project provides a practical and secure solution for hiding sensitive information within images. By prioritizing local processing and offering a user-friendly interface, it empowers users to protect their data while maintaining privacy.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the [MIT License](LICENSE).
