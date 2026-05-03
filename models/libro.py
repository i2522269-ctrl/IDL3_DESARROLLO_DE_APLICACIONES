class Libro:
    def __init__(self, id, titulo, autor, precio_costo, precio_venta, stock):
        self.__id = id
        self.__titulo = titulo
        self.__autor = autor
        self.__precio_costo = precio_costo
        self.__precio_venta = precio_venta
        self.__stock = stock

    @property
    def id(self): return self.__id
    @property
    def titulo(self): return self.__titulo
    @property
    def autor(self): return self.__autor
    @property
    def precio_costo(self): return self.__precio_costo
    @property
    def precio_venta(self): return self.__precio_venta
    @property
    def stock(self): return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock >= 0: self.__stock = nuevo_stock

    def calcular_margen(self):
        return self.__precio_venta - self.__precio_costo

    def valor_inventario(self):
        return self.__precio_costo * self.__stock

    def __str__(self):
        return f"Libro: {self.__titulo} - Stock: {self.__stock}"
