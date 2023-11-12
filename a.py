#Clase Padre
class Usuario:
    def __init__(self, nombre, apellido, edad): #Constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

#Clase-Hijo
class Estudiante(Usuario):
    def __init__(self, nombre, apellido, edad, carreras, clases): #Constructor
        super().__init__(nombre, apellido, edad) # Constructor de clase padre
        self.carreras = carreras
        self.clases = clases

#Clase-Hijo
class Profesor(Usuario):
    def __init__(self, nombre, apellido, edad, carrera, especialidades): # Constructor
        super().__init__(nombre, apellido, edad) #Constructor de clase padre
        self.carrera = carrera
        self.especialidades = especialidades

usuarios = []

#Metodo para ingresar datos de usuario(Estudiante o Profesor)
def ingresar_datos():
    print("Ingrese datos de usuario: ")

    tipo = input("Tipo (E para estudiante, P para profesor): ").upper()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))

    if tipo == "E":
        carreras = input("Carreras(separe con comas): ").split(',')
        clases = input("Clases(separe con comas): ").split(',')
        persona = Estudiante(nombre, apellido, edad, carreras, clases)
    elif tipo == "P":
        carrera = input("Carrera: ")
        especialidades = input("Especialidades(separe con comas): ").split(',')
        persona = Profesor(nombre, apellido, edad, carrera, especialidades)
    else:
        print("Tipo no válido.")
        return
    
    usuarios.append(persona)
    print("\nRegistrado con éxito.")

#Metodo para imprimir los datos del usuario(Estudiante o Profesor)
def imprimir_datos():
    print("\nInformación de personas registradas.")

    for usuario in usuarios:
        if isinstance(usuario, Estudiante):
            tipo = "Estudiante"
            detalles = f"Carreras: {', '.join(usuario.carreras)}, Clases: {', '.join(usuario.clases)}"
        elif isinstance(usuario, Profesor):
            tipo = "Profesor"
            detalles = f"Carrera: {usuario.carrera}, Especialidades: {', '.join(usuario.especialidades)}"
        else:
            tipo = "Desconocido"
            detalles = "Detalles desconocidos"

        print(f"Nombre: {usuario.nombre} {usuario.apellido}")
        print(f"Edad: {usuario.edad}")
        print(f"Tipo: {tipo}")
        print(detalles)
        print()

#Menu Principal
while True:
    try:
        print("\nMenu:")
        print("1. Ingresar datos:")
        print("2. Imprimir datos: ")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))
    except:
        print("***Opción no válida***")
    else:
        if opcion == 1:
            ingresar_datos()
        elif opcion == 2:
            imprimir_datos()
        elif opcion == 3:
            print("Saliendo...")
            break
        else: 
            print("***Opción no válida***")