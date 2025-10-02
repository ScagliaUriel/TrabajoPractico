class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estadoDisponible = True
        self.__prestado_a = None

    def prestar(self, miembro):
        if self.__estadoDisponible:
            self.__estadoDisponible = False
            self.__prestado_a = miembro
            return True
        return False

    def devolver(self):
        self.__estadoDisponible = True
        self.__prestado_a = None

    def get_isbn(self):
        return self.__isbn

    def get_estado(self):
        return self.__estadoDisponible

    def get_autor(self):
        return self.__autor

    def get_titulo(self):
        return self.__titulo

    def get_prestado_a(self):
        return self.__prestado_a

    def __str__(self):
        if self.__estadoDisponible:
            return f"Título: {self.__titulo} - Autor: {self.__autor} - ISBN: {self.__isbn} - Estado: Disponible"
        else:
            return f"Título: {self.__titulo} - Autor: {self.__autor} - ISBN: {self.__isbn} - Estado: Prestado a {self.__prestado_a.get_nombre()}"


class Miembro:
    def __init__(self, nombre, id):
        self.__nombre = nombre
        self.__id = id
        self.__libros_prestados = []

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def pedir_prestado(self, libro):
        if libro.prestar(self):
            self.__libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados and not libro.get_estado():
            libro.devolver()
            self.__libros_prestados.remove(libro)
            return True
        return False

    def __str__(self):
        return f"ID: {self.__id} - Nombre: {self.__nombre}"


class Biblioteca:
    def __init__(self):
        self.__miembros = []
        self.__libros = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def agregar_miembro(self, miembro):
        self.__miembros.append(miembro)

    def eliminar_libro(self, libro):
        if libro in self.__libros:
            self.__libros.remove(libro)

    def eliminar_miembro(self, miembro):
        if miembro in self.__miembros:
            self.__miembros.remove(miembro)

    def libros_disponibles(self):
        return [libro for libro in self.__libros if libro.get_estado()]

    def libros_prestados(self):
        return [libro for libro in self.__libros if not libro.get_estado()]

    def mostrar_miembros(self):
        return [str(m) for m in self.__miembros]

    def mostrar_libros(self):
        return [str(l) for l in self.__libros]
        def buscar_por_autor(self, autor):
            return [libro for libro in self.__libros if libro.get_autor().lower() == autor.lower()]

    def buscar_por_isbn(self, isbn):
        for libro in self.__libros:
            if libro.get_isbn() == isbn:
                return libro
        return None