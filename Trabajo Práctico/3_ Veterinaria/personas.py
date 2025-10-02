class Persona:
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f"{self.__nombre} - DNI: {self.__dni} - Tel: {self.__telefono}"

class Cliente(Persona):
    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)
        self.__mascotas = []

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_mascotas(self):
        if not self.__mascotas:
            print(f"{self.getNombre()} no tiene mascotas registradas.")
        for m in self.__mascotas:
            print(m)

    def getMascotas(self):
        return self.__mascotas

class Veterinario(Persona):
    def __init__(self, dni, nombre, direccion, telefono, matricula, especialidad, disponibilidad=True):
        super().__init__(dni, nombre, direccion, telefono)
        self.__matricula = matricula
        self.__especialidad = especialidad
        self.__disponibilidad = disponibilidad

    def getMatricula(self):
        return self.__matricula

    def getEspecialidad(self):
        return self.__especialidad

    def estaDisponible(self):
        return self.__disponibilidad

    def setDisponibilidad(self, disponible):
        self.__disponibilidad = disponible

    def __str__(self):
        return f"{self.getNombre()} - {self.__especialidad} - Matrícula: {self.__matricula}"