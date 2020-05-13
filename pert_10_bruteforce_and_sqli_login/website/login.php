<?php
include("helpers.php");

if(isset($_SESSION['user_id'])){
    header("Location: index.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h2>Login Form</h2>

    <form action="auth.php" method="POST">
        <input type="hidden" name="token" value="<?= $_SESSION['csrf_token'] ?>">
        <input type="hidden" name="action" value="login">

        <label for="username">Username</label>
        <input type="text" placeholder="Username" name="username" required>

        <label for="password">Password</label>
        <input type="password" placeholder="Password" name="password" required>
    
        <button type="submit">Login</button>

        <?php
        if(isset($_SESSION['message'])){
        ?>
            <div><?= get_message() ?></div>
        <?php
        }
        ?>
    </form>
</div>
</body>
</html>