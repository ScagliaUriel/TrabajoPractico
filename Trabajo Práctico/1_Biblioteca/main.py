from clases import Libro, Miembro, Biblioteca

def mostrar_menu():
    print("\nBIBLIOTECA")
    print("1. Agregar Libro")
    print("2. Agregar Miembro")
    print("3. Prestar Libro")
    print("4. Devolver Libro")
    print("5. Mostrar Todos los Libros")
    print("6. Mostrar Libros Disponibles")
    print("7. Mostrar Libros Prestados")
    print("8. Buscar Libros por Autor")
    print("9. Mostrar Miembros")
    print("0. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)
            print("Libro agregado con éxito.")

        elif opcion == "2":
            nombre = input("Nombre del miembro: ")
            id_miembro = input("ID del miembro: ")
            miembro = Miembro(nombre, id_miembro)
            biblioteca.agregar_miembro(miembro)
            print("Miembro agregado con éxito.")

        elif opcion == "3":
            id_miembro = input("Ingrese ID del miembro: ")
            isbn = input("Ingrese ISBN del libro: ")
            miembro = next((m for m in biblioteca._Biblioteca__miembros if m.get_id() == id_miembro), None)
            libro = next((l for l in biblioteca._Biblioteca__libros if l.get_isbn() == isbn), None)
            if miembro and libro:
                if miembro.pedir_prestado(libro):
                    print("Préstamo realizado.")
                else:
                    print("El libro no está disponible.")
            else:
                print("Miembro o libro no encontrado.")

        elif opcion == "4":
            id_miembro = input("Ingrese ID del miembro: ")
            isbn = input("Ingrese ISBN del libro: ")
            miembro = next((m for m in biblioteca._Biblioteca__miembros if m.get_id() == id_miembro), None)
            libro = next((l for l in biblioteca._Biblioteca__libros if l.get_isbn() == isbn), None)
            if miembro and libro:
                if miembro.devolver_libro(libro):
                    print("Devolución realizada.")
                else:
                    print("El libro no estaba prestado a este miembro.")
            else:
                print("Miembro o libro no encontrado.")

        elif opcion == "5":
            print("\nLista de todos los libros:")
            for l in biblioteca.mostrar_libros():
                print(l)

        elif opcion == "6":
            print("\nLibros disponibles:")
            for l in biblioteca.libros_disponibles():
                print(l)

        elif opcion == "7":
            print("\nLibros prestados:")
            for l in biblioteca.libros_prestados():
                print(l)

        elif opcion == "8":
            autor = input("Ingrese el nombre del autor: ")
            libros = [l for l in biblioteca._Biblioteca__libros if l.get_autor().lower() == autor.lower()]
            if libros:
                for l in libros:
                    print(l)
            else:
                print("No se encontraron libros de ese autor.")

        elif opcion == "9":
            print("\nLista de miembros:")
            for m in biblioteca.mostrar_miembros():
                print(m)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
