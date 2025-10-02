from clases import Estudiante, Curso, Facultad

facultad = Facultad()

while True:
    print("\nFACULTAD")
    print("1. Crear un estudiante")
    print("2. Dar de baja estudiante del sistema")
    print("3. Agregar un curso nuevo")
    print("4. Eliminar un curso")
    print("5. Inscribir un estudiante a un curso")
    print("6. Dar de baja un estudiante de un curso")
    print("7. Consultar cursos (inscriptos y disponibles)")
    print("8. Consultar estudiantes y sus cursos")
    print("0. Salir del sistema")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        matricula = input("Matrícula: ")
        carrera = input("Carrera: ")
        estudiante = Estudiante(nombre, apellido, matricula, carrera)
        facultad.altaEstudiante(estudiante)

    elif opcion == "2":
        matricula = input("Matrícula del estudiante a eliminar: ")
        facultad.bajaEstudiante(matricula)
        print("Estudiante eliminado (si existía).")

    elif opcion == "3":
        nombre = input("Nombre del curso: ")
        codigo = input("Código: ")
        profesor = input("Profesor: ")
        capacidad = int(input("Capacidad: "))
        curso = Curso(nombre, codigo, profesor, capacidad)
        facultad.altaCurso(curso)

    elif opcion == "4":
        codigo = input("Código del curso a eliminar: ")
        facultad.bajaCurso(codigo)

    elif opcion == "5":
        matricula = input("Matrícula del estudiante: ")
        codigo = input("Código del curso: ")
        okE, estudiante = facultad.getEstudiante(matricula)
        okC, curso = facultad.getCurso(codigo)
        if okE and okC:
            estudiante.inscribeCurso(curso)
        else:
            print("Estudiante o curso no encontrado.")

    elif opcion == "6":
        matricula = input("Matrícula del estudiante: ")
        codigo = input("Código del curso: ")
        okE, estudiante = facultad.getEstudiante(matricula)
        okC, curso = facultad.getCurso(codigo)
        if okE and okC:
            estudiante.bajaCurso(curso)
        else:
            print("Estudiante o curso no encontrado.")

    elif opcion == "7":
        facultad.listadoCurso()

    elif opcion == "8":
        facultad.listadoEstudiante()

    elif opcion == "9":
        codigo = input("Código del curso: ")
        ok, curso = facultad.getCurso(codigo)
        if ok:
            curso.listarEstudiantes()
        else:
            print("Curso no encontrado.")  

    elif opcion == "0":
        break

    else:
        print("Opción inválida")