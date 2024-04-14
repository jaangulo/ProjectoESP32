<?php

$GLOBALS["conexion"] = new PDO('mysql:host=localhost; dbname=conexionesp', 'root', '');
$GLOBALS["conexion"] -> exec("set names utf8");

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header("Access-Control-Allow-Headers: X-Requested-With");

$json = file_get_contents('php://input');
$data = json_decode($json);
$led1on = $data->led1on;
$led2on = $data->led2on;

$sq = $conexion -> prepare("INSERT INTO light(led1On, led2on) VALUES ('$led1on','$led2on')");
$sq -> execute();

echo json_encode("ok");

?>