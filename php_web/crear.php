<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agregar Libro - Librería DDA</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { background-color: #f8f9fa; }
        .navbar { background: linear-gradient(45deg, #1d3557, #457b9d); }
        .card { border: none; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark mb-4">
    <div class="container">
        <a class="navbar-brand" href="index.php"><i class="fas fa-book-open me-2"></i>Librería DDA</a>
    </div>
</nav>

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header bg-white py-3">
                    <h4 class="mb-0 text-primary"><i class="fas fa-plus-circle me-2"></i>Registrar Nuevo Libro</h4>
                </div>
                <div class="card-body p-4">
                    <form action="procesar.php" method="POST" class="needs-validation" novalidate>
                        <input type="hidden" name="accion" value="crear">
                        
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label for="sku" class="form-label">SKU / ID</label>
                                <input type="text" class="form-control" id="sku" name="sku" required placeholder="Ej: L003">
                                <div class="invalid-feedback">Por favor ingresa un SKU único.</div>
                            </div>
                            <div class="col-md-6">
                                <label for="stock" class="form-label">Stock Inicial</label>
                                <input type="number" class="form-control" id="stock" name="stock" value="0" min="0" required>
                            </div>
                            
                            <div class="col-12">
                                <label for="titulo" class="form-label">Título del Libro</label>
                                <input type="text" class="form-control" id="titulo" name="titulo" required>
                            </div>
                            
                            <div class="col-12">
                                <label for="autor" class="form-label">Autor</label>
                                <input type="text" class="form-control" id="autor" name="autor" required>
                            </div>
                            
                            <div class="col-md-6">
                                <label for="precio_costo" class="form-label">Precio Costo (S/)</label>
                                <div class="input-group">
                                    <span class="input-group-text">S/</span>
                                    <input type="number" step="0.01" class="form-control" id="precio_costo" name="precio_costo" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <label for="precio_venta" class="form-label">Precio Venta (S/)</label>
                                <div class="input-group">
                                    <span class="input-group-text">S/</span>
                                    <input type="number" step="0.01" class="form-control" id="precio_venta" name="precio_venta" required>
                                </div>
                            </div>
                        </div>

                        <div class="mt-4 d-flex justify-content-between">
                            <a href="index.php" class="btn btn-outline-secondary"><i class="fas fa-arrow-left me-2"></i>Cancelar</a>
                            <button type="submit" class="btn btn-primary px-5">Guardar Libro <i class="fas fa-save ms-2"></i></button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Validación de Bootstrap
(function () {
  'use strict'
  var forms = document.querySelectorAll('.needs-validation')
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
    })
})()
</script>
</body>
</html>
