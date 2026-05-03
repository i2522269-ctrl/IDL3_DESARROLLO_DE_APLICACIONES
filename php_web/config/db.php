<?php
// Configuración de Supabase (Direct Postgres Connection)
$host = "db.xxxx.supabase.co"; // Cambiar por tu host de Supabase
$port = "5432";
$db_name = "postgres";
$username = "postgres";
$password = "tu_contraseña_aqui";

try {
    $conn = new PDO("pgsql:host=$host;port=$port;dbname=$db_name", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $exception) {
    echo "Error de conexión con Supabase: " . $exception->getMessage();
}
?>
