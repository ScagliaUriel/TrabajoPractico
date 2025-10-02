from datetime import datetime

class Venta:
    __contador_id = 1

    def __init__(self, cliente):
        self.__id = Venta.__contador_id
        Venta.__contador_id += 1
        self.__cliente = cliente
        self.__items = []
        self.__fecha = datetime.now()

    def agregarItem(self, producto, cantidad):
        if producto.getStock() >= cantidad:
            producto.restarStock(cantidad)
            self.__items.append((producto, cantidad))
            return True
        return False

    def getCliente(self):
        return self.__cliente

    def getFecha(self):
        return self.__fecha

    def getItems(self):
        return self.__items

    def __str__(self):
        retorno = f"Venta {self.__id} - Cliente: {self.__cliente.getNombre()} - Fecha: {self.__fecha.strftime('%Y-%m-%d %H:%M')}\n"
        total = 0
        for producto, cantidad in self.__items:
            subtotal = producto.getPrecio() * cantidad
            retorno += f"   {producto.getNombre()} x{cantidad} - ${subtotal:.2f}\n"
            total += subtotal
        retorno += f"Total: ${total:.2f}"
        return retorno