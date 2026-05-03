-- Script de creación de base de datos y tabla
CREATE DATABASE IF NOT EXISTS libreria_db;
USE libreria_db;

CREATE TABLE IF NOT EXISTS libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255),
    precio_costo DECIMAL(10,2),
    precio_venta DECIMAL(10,2),
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datos de ejemplo (Opcional)
INSERT INTO libros (sku, titulo, autor, precio_costo, precio_venta, stock) VALUES
('L001', 'El Quijote', 'Miguel de Cervantes', 25.00, 45.00, 10),
('L002', 'Cien Años de Soledad', 'Gabriel García Márquez', 30.00, 55.00, 5);
