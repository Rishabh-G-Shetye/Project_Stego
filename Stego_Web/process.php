<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $action = $_POST['action'];

    if ($action == 'encrypt') {
        $image = $_FILES['image']['tmp_name'];
        $message = $_POST['message'];
        $password = $_POST['password'];

        $command = "python encrypt.py " . escapeshellarg($image) . " " . escapeshellarg($message) . " " . escapeshellarg($password);
        $output = shell_exec($command);

        if (file_exists("encrypted_image.png")) {
            header('Content-Type: image/png');
            header('Content-Disposition: attachment; filename="encrypted_image.png"');
            readfile("encrypted_image.png");
            unlink("encrypted_image.png"); 
        } else {
            echo "Error during encryption.";
        }
    } elseif ($action == 'decrypt') {
        $image = $_FILES['image']['tmp_name'];
        $password = $_POST['password'];

        $command = "python decrypt.py " . escapeshellarg($image) . " " . escapeshellarg($password);
        $output = shell_exec($command);

        echo $output;
    }
}
?>