class Mascota:
    __contador_id = 1

    def __init__(self, nombre, especie, raza="", edad=None):
        self.__id = Mascota.__contador_id
        Mascota.__contador_id += 1
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__historia_clinica = []

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def agregar_historia(self, consulta):
        self.__historia_clinica.append(consulta)

    def getHistoriaClinica(self):
        retorno = ""
        for hc in self.__historia_clinica:
            retorno += hc + "\n"
        return retorno