<?php
$connection = mysqli_connect('127.0.0.1','root','','Techhikka');
if ( $connection == false) {
    echo "Not connected";
    echo mysqli_connect_error();
    exit();
}
$all = mysqli_query($connection,'SELECT * FROM `Users` WHERE `id`=1');
$r1  =  mysqli_fetch_assoc($all);
print_r($r1);
?>

<form method="GET" action="/Registry.php">
    <input type = 'text' placeholder = "Login" name="login">
    <input type = 'password' placeholder = "Password" name = "password">
    <br>
    <input type="submit" value="Enter">
</form>
