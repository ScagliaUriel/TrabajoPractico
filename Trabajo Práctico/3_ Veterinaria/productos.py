class Producto:
    __contador_id = 1

    def __init__(self, nombre, precio, stock=0):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__id = Producto.__contador_id
        Producto.__contador_id += 1
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getPrecio(self):
        return self.__precio

    def getStock(self):
        return self.__stock

    def setPrecio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = precio

    def setStock(self, stock):
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = stock

    def agregarStock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad

    def restarStock(self, cantidad):
        if cantidad > self.__stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.__stock -= cantidad

    def __str__(self):
        return f"[ID {self.__id}] {self.__nombre} - ${self.__precio:.2f} - Stock: {self.__stock}"