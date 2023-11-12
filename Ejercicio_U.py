class Empleado:
    def __init__(self, numero_empleado, nombre):
        self.numero_empleado = numero_empleado
        self.nombre = nombre

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
    def __init__(self, numero_empleado, nombre, fecha_inicio, fecha_fin, bono):
        Administrativo.__init__(self, numero_empleado, nombre, "oficina", "puesto")
        Docente.__init__(self, numero_empleado, nombre, "horario", "departamento")
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.bono = bono

# Crear una lista para almacenar los empleados
empleados = []

# Función para ingresar datos de un empleado
def ingresar_datos():
    print("\nIngresar datos de Empleado: ")
    
    numero_empleado = int(input("No. de Empleado: "))
    nombre = input("Nombre: ")
    tipo_empleado = input("Tipo (A para Administrativo, D para Docente, J para Jefe): ").upper()

    if tipo_empleado == "A":
        oficina = input("Oficina: ")
        puesto = input("Puesto: ")
        empleado = Administrativo(numero_empleado, nombre, oficina, puesto)
    elif tipo_empleado == "D":
        horario = input("Horario: ")
        departamento = input("Departamento: ")
        empleado = Docente(numero_empleado, nombre, horario, departamento)
    elif tipo_empleado == "J":
        fecha_inicio = input("Fecha de inicio como Jefe: ")
        fecha_fin = input("Fecha de fin: ")
        bono = float(input("Bono extra: "))
        empleado = Jefe(numero_empleado, nombre, fecha_inicio, fecha_fin, bono)
    else:
        print("Tipo no válido")
        return
    
    empleados.append(empleado)
    print("Empleado registrado con éxito.")

# Función para imprimir datos de todos los empleados
def imprimir_datos():
    print("Información de empleados registrados: ")
    for empleado in empleados:
        print(f"Empleado: {empleado.numero_empleado}")
        print(f"Nombre: {empleado.nombre}")

        if isinstance(empleado, Administrativo):
            print("Tipo: Administrativo")
            print(f"Oficina: {empleado.oficina}")
            print(f"Puesto: {empleado.puesto}")
        elif isinstance(empleado, Docente):
            print("Tipo: Docente")
            print(f"Horario: {empleado.horario}")
            print(f"Departamento: {empleado.departamento}")
        elif isinstance(empleado, Jefe):
            print("Tipo: Jefe")
            print(f"Fecha de Inicio: {empleado.fecha_inicio}")
            print(f"Fecha de Fin: {empleado.fecha_fin}")
            print(f"Bono extra: {empleado.bono}")
        
        print()

# Función para consultar información de un empleado por número de empleado
def consultar_por_numero_empleado(numero_empleado):
    for empleado in empleados:
        if empleado.numero_empleado == numero_empleado:
            print("Información del empleado con número de empleado:", numero_empleado)
            print(f"Nombre: {empleado.nombre}")
            
            if isinstance(empleado, Administrativo):
                print("Tipo: Administrativo")
                print(f"Oficina: {empleado.oficina}")
                print(f"Puesto: {empleado.puesto}")
            elif isinstance(empleado, Docente):
                print("Tipo: Docente")
                print(f"Horario: {empleado.horario}")
                print(f"Departamento: {empleado.departamento}")
            elif isinstance(empleado, Jefe):
                print("Tipo: Jefe")
                print(f"Fecha de Inicio: {empleado.fecha_inicio}")
                print(f"Fecha de Fin: {empleado.fecha_fin}")
                print(f"Bono extra: {empleado.bono}")
            
            return
    
    print(f"No se encontró un empleado con número de empleado {numero_empleado}.")

# Función para consultar información por departamento
def consultar_por_departamento(departamento):
    print(f"Empleados del departamento: {departamento}")
    for empleado in empleados:
        if isinstance(empleado, Docente) and empleado.departamento == departamento:
            print(f"Empleado: {empleado.numero_empleado}")
            print(f"Nombre: {empleado.nombre}")
            print(f"Tipo: Docente")
            print(f"Horario: {empleado.horario}")
            print(f"Departamento: {empleado.departamento}")
            print()

# Menú principal
while True:
    try:
        print("\nMenú")
        print("1. Ingresar datos")
        print("2. Imprimir datos de empleados")
        print("3. Consultar información por número de empleado")
        print("4. Consultar información por departamento")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Opción no válida")
        continue

    if opcion == 1:
        ingresar_datos()
    elif opcion == 2:
        imprimir_datos()
    elif opcion == 3:
        numero_empleado = int(input("Ingrese el número de empleado: "))
        consultar_por_numero_empleado(numero_empleado)
    elif opcion == 4:
        departamento = input("Ingrese el departamento: ")
        consultar_por_departamento(departamento)
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opción no válida")