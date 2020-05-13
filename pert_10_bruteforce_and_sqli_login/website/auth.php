<?php
include("database.php");
include("helpers.php");

$action = $_REQUEST['action'];

if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_SESSION['csrf_token']) && $_SESSION['csrf_token'] == $_POST['token']){
    $username = $_POST['username'];
    $password = $_POST['password'];

    $query = "SELECT * FROM users WHERE username = '$username' AND PASSWORD = '$password'";
    $sql = $con->query($query);

    if($sql->num_rows > 0){
        $result = $sql->fetch_assoc();
        $_SESSION['user_id'] = $result['id'];

        header("Location: index.php");
    }else{
        set_message("Wrong username or password");
        header("Location: index.php");
    }
}else{
    if($action == 'logout'){
        session_unset();
        session_destroy();
    }

    header("Location: login.php");
}