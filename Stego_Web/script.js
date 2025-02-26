document.getElementById('encryptImage').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('encryptPreview');
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
        };
        reader.readAsDataURL(file);
    } else {
        preview.src = '';
        preview.style.display = 'none';
    }
});

function encrypt() {
    const image = document.getElementById('encryptImage').files[0];
    const message = document.getElementById('secretMessage').value;
    const password = document.getElementById('encryptPassword').value;

    if (!image || !message || !password) {
        alert('Please fill all fields.');
        return;
    }

    const formData = new FormData();
    formData.append('image', image);
    formData.append('message', message);
    formData.append('password', password);
    formData.append('action', 'encrypt');

    fetch('process.php', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'encrypted_image.png';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .catch(error => console.error('Error:', error));
}

function decrypt() {
    const image = document.getElementById('decryptImage').files[0];
    const password = document.getElementById('decryptPassword').value;

    if (!image || !password) {
        alert('Please fill all fields.');
        return;
    }

    const formData = new FormData();
    formData.append('image', image);
    formData.append('password', password);
    formData.append('action', 'decrypt');

    fetch('process.php', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('decryptedMessage').textContent = 'Decrypted Message: ' + data;
    })
    .catch(error => console.error('Error:', error));
}