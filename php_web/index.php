<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Librería - Gestión CRUD</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #f8f9fa; }
        .navbar { background: linear-gradient(45deg, #1d3557, #457b9d); }
        .card { border: none; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .btn-primary { background-color: #457b9d; border: none; }
        .btn-primary:hover { background-color: #1d3557; }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark mb-4">
    <div class="container">
        <a class="navbar-brand" href="#"><i class="fas fa-book-open me-2"></i>Librería DDA</a>
    </div>
</nav>

<div class="container">
    <?php if(isset($_GET['msg'])): ?>
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <i class="fas fa-check-circle me-2"></i>
            <?php 
                if($_GET['msg'] == 'creado') echo "¡Libro registrado con éxito!";
                if($_GET['msg'] == 'actualizado') echo "¡Libro actualizado correctamente!";
                if($_GET['msg'] == 'eliminado') echo "¡Libro eliminado del inventario!";
            ?>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    <?php endif; ?>

    <div class="row mb-3">
        <div class="col-md-6">
            <h3><i class="fas fa-list me-2"></i>Inventario de Libros</h3>
        </div>
        <div class="col-md-6 text-end">
            <a href="crear.php" class="btn btn-primary"><i class="fas fa-plus me-2"></i>Nuevo Libro</a>
        </div>
    </div>

    <div class="card">
        <div class="card-body">
            <div class="table-responsive">
                <table class="table table-hover align-middle">
                    <thead class="table-light">
                        <tr>
                            <th>SKU</th>
                            <th>Título</th>
                            <th>Autor</th>
                            <th>Precio Costo</th>
                            <th>Precio Venta</th>
                            <th>Stock</th>
                            <th class="text-center">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        require_once 'config/db.php';
                        try {
                            $query = "SELECT * FROM libros ORDER BY id DESC";
                            $stmt = $conn->prepare($query);
                            $stmt->execute();
                            
                            if ($stmt->rowCount() > 0) {
                                while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                                    echo "<tr>";
                                    echo "<td>" . htmlspecialchars($row['sku']) . "</td>";
                                    echo "<td>" . htmlspecialchars($row['titulo']) . "</td>";
                                    echo "<td>" . htmlspecialchars($row['autor']) . "</td>";
                                    echo "<td>S/ " . number_format($row['precio_costo'], 2) . "</td>";
                                    echo "<td>S/ " . number_format($row['precio_venta'], 2) . "</td>";
                                    echo "<td>" . htmlspecialchars($row['stock']) . "</td>";
                                    echo "<td class='text-center'>
                                            <a href='editar.php?id=" . $row['id'] . "' class='btn btn-sm btn-warning me-1'><i class='fas fa-edit'></i></a>
                                            <a href='#' onclick='confirmarEliminar(" . $row['id'] . ")' class='btn btn-sm btn-danger'><i class='fas fa-trash'></i></a>
                                          </td>";
                                    echo "</tr>";
                                }
                            } else {
                                echo "<tr><td colspan='7' class='text-center py-4 text-muted'>No hay registros encontrados.</td></tr>";
                            }
                        } catch(PDOException $e) {
                            echo "<tr><td colspan='7' class='text-center text-danger'>Error: " . $e->getMessage() . "</td></tr>";
                        }
                        ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- Scripts -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
function confirmarEliminar(id) {
    if(confirm('¿Estás seguro de que deseas eliminar este registro?')) {
        window.location.href = 'eliminar.php?id=' + id;
    }
}
</script>
</body>
</html>
