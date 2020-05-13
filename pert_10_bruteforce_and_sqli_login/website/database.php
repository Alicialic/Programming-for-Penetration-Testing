<?php
$server = "localhost";
$username = "root";
$password = "";
$database = "pert10";

$con = new mysqli($server, $username, $password, $database);

if($con->connect_error) {
    die("Connection to DB failed");
}