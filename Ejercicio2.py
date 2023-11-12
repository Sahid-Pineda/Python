"""
La universidad desea realizar un sistema para guardar la información de sus estudiantes y profesores,
de los estudiantes se requiere los datos generales y las carreras y clases que esta cursando, de los
profesores se requiere sus datos generales y la carrera en la que trabaja y las áreas de especialidad 
en las que trabaja e imparte clases, realizar el sistema para capturas la información y mostrar la misma. 
"""

class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, edad, carrera, clases):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera
        self.clases = clases

class Profesor(Usuario):
    def __init__(self, nombre, apellido, edad, carrera, especialidades):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera
        self.especialidades = especialidades

estudiante1 = Estudiante("Chris", "Pineda", 19, ["Fisica"], ["Matematicas", "Algebra"])

profesor1 = Profesor("Fernando", "Meza", 43, ["Matematicas"], ["Algebra", "Calculo"])


print("\nEstudiantes: ")
for estudiante in [estudiante1]:
    print(f"Nombre: {estudiante.nombre} {estudiante.apellido}")
    print(f"Edad: {estudiante.edad}")
    print(f"Carrera: {', '.join(estudiante.carrera)}")
    print(f"Clases: {', '.join(estudiante.clases)}")


print("\nProfesores: ")
for profesor in [profesor1]:
    print(f"Nombre: {profesor.nombre} {profesor.apellido}")
    print(f"Edad: {profesor.edad}")
    print(f"Carrera: {', '.join(profesor.carrera)}")
    print(f"Clases: {', '.join(profesor.especialidades)}")