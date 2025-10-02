from datetime import datetime

class Turno:
    __contador_id = 1

    def __init__(self, cliente, mascota, veterinario, fecha_hora):
        self.__id = Turno.__contador_id
        Turno.__contador_id += 1
        self.__cliente = cliente
        self.__mascota = mascota
        self.__veterinario = veterinario
        if isinstance(fecha_hora, str):
            self.__fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
        else:
            self.__fecha_hora = fecha_hora

    def getId(self):
        return self.__id

    def getMascota(self):
        return self.__mascota

    def getVeterinario(self):
        return self.__veterinario

    def getCliente(self):
        return self.__cliente

    def getFechaHora(self):
        return self.__fecha_hora

    def __str__(self):
        fecha_str = self.__fecha_hora.strftime("%Y-%m-%d %H:%M")
        return f"Turno {self.__id}: {self.__mascota.getNombre()} con {self.__veterinario.getNombre()} el {fecha_str}"