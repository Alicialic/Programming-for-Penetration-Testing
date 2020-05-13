<?php
session_start();

if(!isset($_SESSION['csrf_token'])){
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

function set_message($message){
    $_SESSION['message'] = $message;
}

function get_message(){
    if(isset($_SESSION['message'])){
        $message = $_SESSION['message']; 
        $_SESSION['message'] = '';
        return $message;
    }
}