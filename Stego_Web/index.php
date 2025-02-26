<!DOCTYPE html>
<html>
<head>
    <title>Steganography Converter</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Steganography Converter</h1>

        <div class="section">
            <h2>Encrypt Image</h2>
            <input type="file" id="encryptImage" accept="image/*">
            <img id="encryptPreview" style="max-width: 300px; display: none;">
            <input type="text" id="secretMessage" placeholder="Secret Message">
            <input type="password" id="encryptPassword" placeholder="Password">
            <button onclick="encrypt()">Encrypt</button>
        </div>

        <div class="section">
            <h2>Decrypt Image</h2>
            <input type="file" id="decryptImage" accept="image/*">
            <input type="password" id="decryptPassword" placeholder="Password">
            <button onclick="decrypt()">Decrypt</button>
            <p id="decryptedMessage"></p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>