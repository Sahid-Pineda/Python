class Empleado:
    _numero_empleado = None
    _nombre= None

    def __init__(self, numero_empleado, nombre):
        self._numero_empleado = numero_empleado
        self._nombre = nombre

class Administrativo(Empleado):
    oficina = None
    puesto = None

    def __init__(self, numero_empleado, nombre):
        super().__init__(numero_empleado, nombre)
        
    def obtener_tipo(self):
        return "Administrativo"

class Docente(Empleado):
    horario = None
    departamento = None

    def __init__(self, numero_empleado, nombre, oficina):
        super().__init__(numero_empleado, nombre, oficina)

    def obtener_tipo(self):
        return "Docente"
    
class Jefe(Administrativo, Docente):
    fecha_inicio = None
    fecha_fin = None
    bono = None

    def __init__(self, numero_empleado, nombre):
        super().__init__(numero_empleado, nombre)

    def obtener_tipo(self):
        return "Jefe"

empleados = []

def ingresar_datos():
    print("\nIngresar datos de Usuario: ")

    tipo = input("Tipo (A para administrativo, D para Docente y J para jefe): ").upper()
    numero_empleado = int(input("No de Empleado:"))
    nombre = input("Nombre: ")

    if tipo == "A":
        oficina = input("Oficina: ")
        puesto = input("Puesto: ")
        empleado = Administrativo(numero_empleado, nombre)
    elif tipo == "D":
        horario = input("Horario: ")
        departamento = input("Departamento: ")
        empleado = Docente(numero_empleado, nombre)
    elif tipo == "J":
        fecha_inicio = input("Fecha de inicio: ")
        fecha_fin = input("Fecha Fin: ")
        bono = float(input("Bono:"))
        empleado = Jefe(numero_empleado, nombre)
    else:
        print("Tipo no valido")

    empleados.append(empleado)
    print("Empleado registrado con éxito.")

def imprimir_datos():
    print("Informacion de empleados registrados: ")
    for empleado in empleados:
        if isinstance(empleado, Administrativo):
            tipo = "Administrativo"
            detalles = f"Oficina: {empleado.oficina} Puesto: {empleado.puesto}"
        elif isinstance(empleado, Docente):
            tipo = "Docente"
            detalles = f"Horario: {empleado.horario} Departamento: {empleado.departamento}"
        elif isinstance(empleado, Jefe):
            tipo = "Jefe"
            detalles = f"Fecha de Inicio: {empleado.fecha_inicio} Fecha Fin: {empleado.fecha_fin} Bono: {empleado.bono}"
        else:
            print("Tipo Desconocido")
            print("Detaller Desconocidos")
        
        print(f"Empleado: {empleado._numero_empleado}")
        print(f"Nombre: {empleado._nombre}")
        print(f"Tipo: {tipo}")
        print(detalles)
        print()

while True:
    try: 
        print("\nMenú")
        print("1. Ingresar datos")
        print("2. Imprimir datos")
        print("3. Salir")
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("Opcion no valida")
    else:
        if opcion == 1:
            ingresar_datos()
        elif opcion == 2:
            imprimir_datos()
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")



