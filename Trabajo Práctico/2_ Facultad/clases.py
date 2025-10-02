class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__profesor = profesor
        self.__capacidad = int(capacidad)
        self.__estudiantesInscriptos = []

    def agregarEstudiante(self, estudiante):
        if self.cuposDisponibles() and estudiante not in self.__estudiantesInscriptos:
            self.__estudiantesInscriptos.append(estudiante)
            return True
        return False

    def sacarEstudiante(self, estudiante):
        if estudiante in self.__estudiantesInscriptos:
            self.__estudiantesInscriptos.remove(estudiante)
            return True
        return False

    def cuposDisponibles(self):
        return self.__capacidad > len(self.__estudiantesInscriptos)

    def getCodigo(self):
        return self.__codigo

    def listarEstudiantes(self):
        if self.__estudiantesInscriptos:
            print(f"Estudiantes en {self.__nombre}:")
            for e in self.__estudiantesInscriptos:
                print(f"   {e.getMatricula()} - {e}")
        else:
            print(f"No hay estudiantes inscriptos en {self.__nombre}.")


    def __str__(self):
        return f"Código: {self.__codigo} - Nombre: {self.__nombre} - Profesor: {self.__profesor} - Inscriptos: {len(self.__estudiantesInscriptos)} - Cupos disponibles: {self.__capacidad - len(self.__estudiantesInscriptos)}"


class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__matricula = matricula
        self.__carrera = carrera
        self.__cursos = []

    def inscribeCurso(self, curso):
        if curso.agregarEstudiante(self):
            self.__cursos.append(curso)
            print(f"El estudiante {self.__nombre} {self.__apellido} se inscribió en {curso.getCodigo()}")
        else:
            print("No fue posible inscribir: curso lleno o ya inscripto.")

    def bajaCurso(self, curso):
        if curso.sacarEstudiante(self):
            self.__cursos.remove(curso)

    def getMatricula(self):
        return self.__matricula

    def __str__(self):
        retorno = f"{self.__matricula} - Nombre: {self.__apellido}, {self.__nombre} - Carrera: {self.__carrera}\n"
        for curso in self.__cursos:
            retorno += f"   {curso}\n"
        return retorno


class Facultad:
    def __init__(self):
        self.__estudiantes = []
        self.__cursos = []

    def altaEstudiante(self, estudiante):
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)

    def bajaEstudiante(self, matricula):
        ok, estudiante = self.getEstudiante(matricula)
        if ok:
            self.__estudiantes.remove(estudiante)

    def getEstudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.getMatricula() == matricula:
                return True, estudiante
        return False, None

    def altaCurso(self, curso):
        if curso not in self.__cursos:
            self.__cursos.append(curso)

    def bajaCurso(self, codigo):
        ok, curso = self.getCurso(codigo)
        if ok:
            self.__cursos.remove(curso)

    def getCurso(self, codigo):
        for curso in self.__cursos:
            if curso.getCodigo() == codigo:
                return True, curso
        return False, None

    def listadoCurso(self):
        for curso in self.__cursos:
            print(curso)

    def listadoEstudiante(self):
        for estudiante in self.__estudiantes:
            print(estudiante)