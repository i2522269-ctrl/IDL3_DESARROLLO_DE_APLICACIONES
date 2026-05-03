<?php
// Configuración básica para Supabase
$host = "tu-proyecto.supabase.co";
$port = "5432";
$db_name = "postgres";
$user = "postgres";
$pass = "tu-password";

try {
    $pdo = new PDO("pgsql:host=$host;port=$port;dbname=$db_name", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Para empezar, solo mostraremos si hay error
    die("Error de conexión: " . $e->getMessage());
}
?>
