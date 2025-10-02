from personas import Cliente, Veterinario
from mascotas import Mascota
from productos import Producto
from turnos import Turno
from ventas import Venta

class Clinica:
    def __init__(self):
        self.__clientes = []
        self.__veterinarios = []
        self.__mascotas = []
        self.__productos = []
        self.__turnos = []
        self.__ventas = []

    def agregarCliente(self, cliente: Cliente):
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)

    def buscarCliente(self, dni: str):
        for c in self.__clientes:
            if c.getDni() == dni:
                return c
        return None

    def eliminarCliente(self, dni: str):
        cliente = self.buscarCliente(dni)
        if cliente:
            self.__clientes.remove(cliente)

    def modificarCliente(self, dni: str, direccion: str, telefono: str):
        cliente = self.buscarCliente(dni)
        if cliente:
            cliente.setDireccion(direccion)
            cliente.setTelefono(telefono)

    def agregarVeterinario(self, veterinario: Veterinario):
        if veterinario not in self.__veterinarios:
            self.__veterinarios.append(veterinario)

    def buscarVeterinario(self, dni: str):
        for v in self.__veterinarios:
            if v.getDni() == dni:
                return v
        return None

    def eliminarVeterinario(self, dni: str):
        vet = self.buscarVeterinario(dni)
        if vet:
            self.__veterinarios.remove(vet)

    def agregarMascota(self, mascota: Mascota, cliente: Cliente):
        cliente.agregar_mascota(mascota)
        if mascota not in self.__mascotas:
            self.__mascotas.append(mascota)

    def buscarMascota(self, id: int):
        for m in self.__mascotas:
            if m.getId() == id:
                return m
        return None

    def eliminarMascota(self, id: int):
        mascota = self.buscarMascota(id)
        if mascota:
            for cliente in self.__clientes:
                if mascota in cliente.getMascotas():
                    cliente.getMascotas().remove(mascota)
            self.__mascotas.remove(mascota)

    def agregarProducto(self, producto: Producto):
        if producto not in self.__productos:
            self.__productos.append(producto)

    def buscarProducto(self, nombre: str):
        for p in self.__productos:
            if p.getNombre() == nombre:
                return p
        return None

    def eliminarProducto(self, nombre: str):
        producto = self.buscarProducto(nombre)
        if producto:
            self.__productos.remove(producto)

    def agendarTurno(self, turno: Turno):
        self.__turnos.append(turno)

    def cancelarTurno(self, id_turno: int):
        self.__turnos = [t for t in self.__turnos if t.getId() != id_turno]

    def listadoTurnosPorVeterinario(self, dni: str):
        return [t for t in self.__turnos if t.getVeterinario().getDni() == dni]

    def listadoTurnosPorMascota(self, id_mascota: int):
        return [t for t in self.__turnos if t.getMascota().getId() == id_mascota]

    def registrarVenta(self, venta: Venta):
        self.__ventas.append(venta)

    def listadoVentas(self):
        return self.__ventas

    def listadoClientes(self):
        return self.__clientes

    def listadoVeterinarios(self):
        return self.__veterinarios

    def listadoMascotas(self):
        return self.__mascotas

    def listadoProductos(self):
        return self.__productos