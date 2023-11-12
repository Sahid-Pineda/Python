def mostrar_comida(comida):
    return f"Nombre: {comida['nombre']}, Tipo: {comida['tipo']}"

def cc_comida():
    mostrado = False
    for comida in comidas:
        if nombre_comida == comida['nombre']:
            print(mostrar_comida(comida))
            mostrado = True

    if not mostrado:
        print("XXXXXXX Comida no encontrada XXXXXXXX")
    else:
        print('----- Para salir debe ingresar la palabra "Salir" en el nombre del ingrediente -----')

comidas = []
indice = 0
seguir = True
opcion = 0

while(seguir):
    try:
        print("\n********Menu*********")
        print("1. Ingrese Comida")
        print("2. Mostrar todas las comidas")
        print("3. Mostrar una Comida")
        print("4. Agregar Ingredientes")
        print("5. Agregar Receta")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion ==> "))
    except:
        print("XXXXX Opcion no valida XXXXXX")
    else:
        match opcion:
            case 1:
                comida = {}
                print("*****Ingrese Comida******")
                comida['nombre'] = input("Nombre de la comida: ")
                comida['tipo'] = input("Tipo de comida: ")
                comidas.append(comida)
                print("Comida ingresada con éxito")
            case 2:
                print(f"****Comida {len(comidas)}*******")
                contador = 1

                for comida in comidas:
                    print(f"Comida {contador}")
                    print(mostrar_comida(comida))
                    contador += 1
            case 3:
                print(f"*******Mostrar información de una comida*****")
                nombre_comida = input('Ingrese nombre de la comida: ')

                mostrado = False
                for comida in comidas:
                    if nombre_comida == comida['nombre']:
                        print(mostrar_comida(comida))
                        mostrado = True
                if not mostrado:
                    print("****** Comida no encontrada ******")
            case 4:
                print(f"***** Agregar ingredientes de una comida *****")
                nombre_comida = input('Ingrese nombre de la comida: ')

                cc_comida()
                ingredientes = []
                ingresar = True
                while(ingresar):
                    ingrediente = {}
                    ingrediente['nombre'] = input('Nombre del ingrediente: ')
                    if ingrediente['nombre'] == "Salir":
                        ingresar = False
                        continue;

                    try:
                        ingrediente['costo'] = float(input("Costo del Ingrediente: "))
                        ingrediente['cantidad'] = float(input('Cantidad del Ingrediente: '))
                        ingrediente['um'] = input("UM del ingrediente: ")
                        ingredientes.append(ingrediente)
                    except:
                        print("XXXXX Valor tiene que se decimal XXXXXXXX")
                    else:
                        print("Ingrediente ingresado con éxito")
                comidas[indice]['ingredientes'] = ingredientes

            case 5:
                print(f"****** Agregar receta de una comida *******")
                nombre_comida = input('Ingrese nombre de la comida: ')

                cc_comida()
                pasos = []
                ingresar = True
                while(ingresar):
                    descripcion = input('Ingrese descripcion: ')

                    if descripcion == "Salir":
                        ingresar = False
                        continue;
                    else:
                        pasos.append(descripcion)

                comidas[indice]['receta'] = pasos
            case 6:
                print("*****Hasta luego*****")
                seguir = False
            case default:
                print("XXXX Opcion no valida XXXXXXXX")
