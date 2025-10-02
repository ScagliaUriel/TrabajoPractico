from clinica import Clinica
from personas import Cliente, Veterinario
from mascotas import Mascota
from productos import Producto
from turnos import Turno
from ventas import Venta
from datetime import datetime

def menu():
    clinica = Clinica()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Cliente")
        print("2. Registrar Veterinario")
        print("3. Registrar Mascota")
        print("4. Registrar Producto")
        print("5. Agendar Turno")
        print("6. Cancelar Turno")
        print("7. Registrar Venta")
        print("8. Listar Turnos por Veterinario")
        print("9. Listar Turnos por Mascota")
        print("10. Listar Ventas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            cliente = Cliente(dni, nombre, direccion, telefono)
            clinica.agregarCliente(cliente)
            print("Cliente registrado.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            matricula = input("Matrícula: ")
            especialidad = input("Especialidad: ")
            disponibilidad = input("Disponibilidad: ")
            veterinario = Veterinario(dni, nombre, direccion, telefono, matricula, especialidad, disponibilidad)
            clinica.agregarVeterinario(veterinario)
            print("Veterinario registrado.")

        elif opcion == "3":
            dni = input("DNI del dueño: ")
            cliente = clinica.buscarCliente(dni)
            if cliente:
                nombre = input("Nombre de la mascota: ")
                especie = input("Especie: ")
                raza = input("Raza: ")
                edad = int(input("Edad: "))
                mascota = Mascota(nombre, especie, raza, edad)
                clinica.agregarMascota(mascota, cliente)
                print("Mascota registrada.")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            producto = Producto(nombre, precio, stock)
            clinica.agregarProducto(producto)
            print("Producto registrado.")

        elif opcion == "5":
            dni_vet = input("DNI del veterinario: ")
            vet = clinica.buscarVeterinario(dni_vet)
            if vet:
                id_mascota = int(input("ID de la mascota: "))
                mascota = clinica.buscarMascota(id_mascota)
                if mascota:
                    fecha_hora_str = input("Fecha y hora (YYYY-MM-DD HH:MM): ")
                    try:
                        fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
                        cliente = None
                        for c in clinica._Clinica__clientes:
                            if mascota in c.getMascotas():
                                cliente = c
                                break
                        turno = Turno(cliente, mascota, vet, fecha_hora)
                        clinica.agendarTurno(turno)
                        print("Turno agendado.")
                    except ValueError:
                        print("Formato de fecha/hora incorrecto.")
                else:
                    print("Mascota no encontrada.")
            else:
                print("Veterinario no encontrado.")

        elif opcion == "6":
            id_turno = int(input("ID del turno a cancelar: "))
            clinica.cancelarTurno(id_turno)
            print("Turno cancelado.")

        elif opcion == "7":
            dni = input("DNI del cliente: ")
            cliente = clinica.buscarCliente(dni)
            if cliente:
                venta = Venta(cliente)
                while True:
                    nombre_prod = input("Producto (ENTER para terminar): ")
                    if nombre_prod == "":
                        break
                    producto = clinica.buscarProducto(nombre_prod)
                    if producto:
                        cantidad = int(input("Cantidad: "))
                        if venta.agregarItem(producto, cantidad):
                            print("Producto agregado.")
                        else:
                            print("Stock insuficiente.")
                    else:
                        print("Producto no encontrado.")
                clinica.registrarVenta(venta)
                print("Venta registrada.")
                print(venta)
            else:
                print("Cliente no encontrado.")

        elif opcion == "8":
            dni = input("DNI del veterinario: ")
            turnos = clinica.listadoTurnosPorVeterinario(dni)
            for t in turnos:
                print(t)

        elif opcion == "9":
            id_mascota = int(input("ID de la mascota: "))
            turnos = clinica.listadoTurnosPorMascota(id_mascota)
            for t in turnos:
                print(t)

        elif opcion == "10":
            for v in clinica.listadoVentas():
                print(v)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()