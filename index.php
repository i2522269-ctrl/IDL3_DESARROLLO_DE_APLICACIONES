<?php require_once 'config.php'; ?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>CRUD Simple - Supabase</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5">
    <div class="container">
        <h1>Gestión de Libros</h1>
        <hr>
        
        <!-- Formulario Simple -->
        <div class="card mb-4">
            <div class="card-body">
                <form action="guardar.php" method="POST">
                    <div class="row">
                        <div class="col"><input type="text" name="titulo" class="form-control" placeholder="Título" required></div>
                        <div class="col"><input type="text" name="autor" class="form-control" placeholder="Autor" required></div>
                        <div class="col"><button type="submit" class="btn btn-success w-100">Agregar</button></div>
                    </div>
                </form>
            </div>
        </div>

        <!-- Tabla Simple -->
        <table class="table border">
            <thead>
                <tr>
                    <th>Título</th>
                    <th>Autor</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Consulta simple
                $stmt = $pdo->query("SELECT * FROM libros ORDER BY id DESC");
                while ($row = $stmt->fetch()) {
                    echo "<tr>
                            <td>{$row['titulo']}</td>
                            <td>{$row['autor']}</td>
                            <td>
                                <a href='borrar.php?id={$row['id']}' class='btn btn-danger btn-sm'>Borrar</a>
                            </td>
                          </tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>
