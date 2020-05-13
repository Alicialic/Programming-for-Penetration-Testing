<?php
include("helpers.php");

if(!isset($_SESSION['user_id'])){
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <a href="auth.php?action=logout">Logout</a>
    <h2>This is homepage</h2>
</div>

</body>
</html>