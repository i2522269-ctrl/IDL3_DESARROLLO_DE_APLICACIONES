class Libro:
    def __init__(self, titulo, autor, precio_costo, precio_venta, stock, sku=None, id=None):
        self.id = id
        self.sku = sku
        self.titulo = titulo
        self.autor = autor
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.stock = stock

    def __str__(self):
        return f"{self.titulo} - {self.autor} (Stock: {self.stock})"

    def calcular_subtotal_costo(self):
        return self.precio_costo * self.stock
