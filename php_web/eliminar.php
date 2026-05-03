<?php
require_once 'config/db.php';

if (isset($_GET['id'])) {
    $id = $_GET['id'];

    try {
        $stmt = $conn->prepare("DELETE FROM libros WHERE id = ?");
        $stmt->execute([$id]);
        header("Location: index.php?msg=eliminado");
    } catch(PDOException $e) {
        die("Error al eliminar: " . $e->getMessage());
    }
} else {
    header("Location: index.php");
}
?>
