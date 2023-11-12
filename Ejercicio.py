"""
La universidad desea realizar un sistema para poder llevar el control de sus empleados
para esto se requiera almacenar los datos generales de cada uno mas el numero de empleado,
cada empleado puede ser administrativo o docente, en caso de ser administrativo tendra un 
puesto asignado y una oficina, en el caso de los docentes tendran un departamento asignado
y un horario, asi mismo se requiere ingresar a los jefes de cada departamento por lo cual 
este jefe tendra que ser un administrativo y docente al mismo tiempo, en el jefe se requiere 
una fecha de inicio como jefe y una fecha fin, asi como un valor que almacenara el bono extra 
de salario que el tendra, se desean ingresar los empleados asi como consultar informacion por 
departamento e individual por numero de empleado
"""

class Empleado:
    def __init__(self, numero_empleado, nombre):
        self._numero_empleado = numero_empleado
        self._nombre = nombre

class Administrativo(Empleado):
    def __init__(self, numero_empleado, nombre, oficina, puesto):
        super().__init__(numero_empleado, nombre)
        self.oficina = oficina
        self.puesto = puesto

class Docente(Empleado):
    def __init__(self, numero_empleado, nombre, horario, departamento):
        super().__init__(numero_empleado, nombre)
        self.horario = horario
        self.departamento = departamento
    
class Jefe(Administrativo, Docente):
    def __init__(self, numero_empleado, nombre, fecha_inicio, fecha_fin, bono, oficina, puesto, horario, departamento):
        Administrativo.__init__(self, numero_empleado, nombre, oficina, puesto)
        Docente.__init__(self, numero_empleado, nombre, horario, departamento)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.bono = bono

empleados = []

def ingresar_datos():
    print("\nIngresar datos de Usuario: ")

    numero_empleado = int(input("No de Empleado:"))
    nombre = input("Nombre: ")
    tipo = input("Tipo (A para administrativo, D para Docente y J para jefe): ").upper()

    if tipo == "A":
        oficina = input("Oficina: ")
        puesto = input("Puesto: ")
        empleado = Administrativo(numero_empleado, nombre, oficina, puesto)
    elif tipo == "D":
        horario = input("Horario: ")
        departamento = input("Departamento: ")
        empleado = Docente(numero_empleado, nombre, horario, departamento)
    elif tipo == "J":
        puesto = input("Puesto: ")
        departamento = input("Departamento: ")
        fecha_inicio = input("Fecha de inicio: ")
        fecha_fin = input("Fecha Fin: ")
        bono = float(input("Bono:"))
        empleado = Jefe(numero_empleado, nombre, fecha_inicio, fecha_fin, bono)
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
