class Comida:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.ingredientes = []
        self.receta = []

    def agregar_ingrediente(self, nombre, costo, cantidad, um):
        ingrediente = {
            'nombre': nombre,
            'costo': costo,
            'cantidad': cantidad,
            'um': um
        }
        self.ingredientes.append(ingrediente)

    def agregar_paso_receta(self, descripcion):
        self.receta.append(descripcion)

def mostrar_comida(comida):
    print(f"Nombre: {comida.nombre}, Tipo: {comida.tipo}")

def mostrar_ingredientes(comida):
    if comida.ingredientes:
        print("Ingredientes:")
        for ingrediente in comida.ingredientes:
            print(f"Nombre: {ingrediente['nombre']}, Costo: {ingrediente['costo']}, Cantidad: {ingrediente['cantidad']}, UM: {ingrediente['um']}")
    else:
        print("No hay ingredientes registrados para esta comida.")

def mostrar_receta(comida):
    if comida.receta:
        print("Receta:")
        for paso, descripcion in enumerate(comida.receta, 1):
            print(f"Paso {paso}: {descripcion}")
    else:
        print("No hay receta registrada para esta comida.")

comidas = []
seguir = True

while seguir:
    try:
        print("\n********Menu*********")
        print("1. Ingrese Comida")
        print("2. Mostrar todas las comidas")
        print("3. Mostrar una Comida")
        print("4. Agregar Ingredientes")
        print("5. Agregar Receta")
        print("6. Mostrar Ingredientes de una Comida")
        print("7. Mostrar Receta de una Comida")
        print("8. Salir")
        opcion = int(input("Seleccione una opcion ==> "))
    except ValueError:
        print("XXXXX Opcion no valida XXXXXX")
        continue

    if opcion == 1:
        nombre = input("Nombre de la comida: ")
        tipo = input("Tipo de comida: ")
        comida = Comida(nombre, tipo)
        comidas.append(comida)
        print("Comida ingresada con éxito")

    elif opcion == 2:
        print("****Comidas registradas****")
        for i, comida in enumerate(comidas, 1):
            print(f"Comida {i}")
            mostrar_comida(comida)

    elif opcion == 3:
        print("***** Mostrar información de una comida *****")
        nombre_comida = input('Ingrese nombre de la comida: ')
        found = False
        for comida in comidas:
            if nombre_comida == comida.nombre:
                mostrar_comida(comida)
                found = True
                break
        if not found:
            print("****** Comida no encontrada ******")

    elif opcion == 4:
        print("***** Agregar ingredientes de una comida *****")
        nombre_comida = input('Ingrese nombre de la comida: ')
        found = False
        for comida in comidas:
            if nombre_comida == comida.nombre:
                mostrar_ingredientes(comida)
                while True:
                    ingrediente_nombre = input('Nombre del ingrediente (o "Salir" para finalizar): ')
                    if ingrediente_nombre.lower() == "salir":
                        break
                    costo = float(input("Costo del Ingrediente: "))
                    cantidad = float(input('Cantidad del Ingrediente: '))
                    um = input("UM del ingrediente: ")
                    comida.agregar_ingrediente(ingrediente_nombre, costo, cantidad, um)
                    print("Ingrediente ingresado con éxito")
                found = True
                break
        if not found:
            print("****** Comida no encontrada ******")

    elif opcion == 5:
        print("****** Agregar receta de una comida *******")
        nombre_comida = input('Ingrese nombre de la comida: ')
        found = False
        for comida in comidas:
            if nombre_comida == comida.nombre:
                mostrar_receta(comida)
                while True:
                    descripcion = input('Ingrese descripcion (o "Salir" para finalizar): ')
                    if descripcion.lower() == "salir":
                        break
                    comida.agregar_paso_receta(descripcion)
                found = True
                break
        if not found:
            print("****** Comida no encontrada ******")

    elif opcion == 6:
        print("***** Mostrar ingredientes de una comida *****")
        nombre_comida = input('Ingrese nombre de la comida: ')
        found = False
        for comida in comidas:
            if nombre_comida == comida.nombre:
                mostrar_ingredientes(comida)
                found = True
                break
        if not found:
            print("****** Comida no encontrada ******")

    elif opcion == 7:
        print("****** Mostrar receta de una comida *******")
        nombre_comida = input('Ingrese nombre de la comida: ')
        found = False
        for comida in comidas:
            if nombre_comida == comida.nombre:
                mostrar_receta(comida)
                found = True
                break
        if not found:
            print("****** Comida no encontrada ******")

    elif opcion == 8:
        print("*****Hasta luego*****")
        seguir = False

    else:
        print("XXXX Opcion no valida XXXXXXXX")
