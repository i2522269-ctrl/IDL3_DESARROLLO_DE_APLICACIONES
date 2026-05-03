<?php
require_once 'config/db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $accion = $_POST['accion'];

    if ($accion == "crear") {
        $sku = $_POST['sku'];
        $titulo = $_POST['titulo'];
        $autor = $_POST['autor'];
        $precio_costo = $_POST['precio_costo'];
        $precio_venta = $_POST['precio_venta'];
        $stock = $_POST['stock'];

        try {
            $stmt = $conn->prepare("INSERT INTO libros (sku, titulo, autor, precio_costo, precio_venta, stock) VALUES (?, ?, ?, ?, ?, ?)");
            $stmt->execute([$sku, $titulo, $autor, $precio_costo, $precio_venta, $stock]);
            header("Location: index.php?msg=creado");
        } catch(PDOException $e) {
            die("Error al insertar: " . $e->getMessage());
        }
    }

    if ($accion == "editar") {
        $id = $_POST['id'];
        $sku = $_POST['sku'];
        $titulo = $_POST['titulo'];
        $autor = $_POST['autor'];
        $precio_costo = $_POST['precio_costo'];
        $precio_venta = $_POST['precio_venta'];
        $stock = $_POST['stock'];

        try {
            $stmt = $conn->prepare("UPDATE libros SET sku = ?, titulo = ?, autor = ?, precio_costo = ?, precio_venta = ?, stock = ? WHERE id = ?");
            $stmt->execute([$sku, $titulo, $autor, $precio_costo, $precio_venta, $stock, $id]);
            header("Location: index.php?msg=actualizado");
        } catch(PDOException $e) {
            die("Error al actualizar: " . $e->getMessage());
        }
    }
} else {
    header("Location: index.php");
}
?>
