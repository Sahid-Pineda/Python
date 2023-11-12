"""Un restaurante desea un sistema para almacenarla comida que prepara, de la comida se desea el nombre
del plato, el tipo de plato que puede ser ensalada, carnes, hamburguesas etc., así mismo la comida 
tendrá una lista de ingredientes y las cantidades que se usa de cada ingrediente la unidad de medida 
y el costo por unidad de medida. de cada comida se desea saber la receta, en la cual se describe paso 
a paso la preparación, para lo cual se desea el orden en el que se realizan los pasos y la descripción de este.
la forma de ingreso de los datos es que primero ingresan la comida luego, a esta comida se le ingresaran 
los ingredientes mediante otro item del menu, de igual forma se realiza con la receta, se debera mostrar 
el listado de todas las comidas y poder ver una comida en especifico"""

def mostrar_comida(comida):
    return f"Nombre : {comida['nombre']}, Tipo: {comida['tipo']}"

comidas = []
opcion = 0
seguir = True

while(seguir):
    try:
        print("\n***** Menu *****")
        print("1. Agregar Comida")
        print("2. Mostrar comidas")
        print("3. Mostar una comida")
        print("4. Agregar Ingredientes")
        print("5. Agregar receta")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))
    except:
        print("***** Opción no válida *****")
    else:
        match opcion:
            case 1:
                comida = {}
                print("***** Agregar comida *****")
                comida['nombre'] = input("Ingrese nombre de la comida: ")
                comida['tipo'] = input("Ingrese el tipo de comida: ")
                comidas.append(comida)
                print("---Comida agregada con éxito---")
            case 2:
                print(f"***** Comidas {len(comida)}")
                contador = 1

                for comida in comidas:
                    print(f'comida {contador}')
                    print(mostrar_comida(comida))
                    contador += 1

            case 3:
                print("***** Mostrar una comida *****")
                nombre_comida = input("Ingrese el nombre de la comida: ")

                encontrada = False
                for comida in comidas:
                    if  nombre_comida == comida['nombre']:
                        print(mostrar_comida(comida))
                        encontrada = True
                if not encontrada:
                    print("Comida no encontrada: ")
            case 4:
                print("***** Agregar ingredientes *****")
                nombre_comida = input("Ingrese nombre de la comida: ")
                
                indice = 0
                encontrada = False
                for comida in comidas:
                    if  nombre_comida == comida['nombre']:
                        print(mostrar_comida(comida))
                        encontrada = True
                        
                    if not encontrada:
                        indice += 1

                if not encontrada:
                    print("***** Comida no encontrada *****")
                else:
                    print('***** Para salir debe ingresar la palabra "salir" en el nombre del ingrediente ')

                    ingredientes = []
                    ingresar = True
                    while(ingresar):
                        ingrediente = {}
                        ingrediente['nombre'] = input("Ingrese el nombre del ingrediente: ")
                        if ingrediente['nombre'] == "Salir":
                            ingresar = False
                            continue;
                        
                        try:
                            ingrediente['cantidad'] = float(input("Ingresar cantidad de ingredientes: "))
                            ingrediente['costo'] = float(input("Ingresar costo de ingredientes: "))
                            ingrediente['um'] = input("Ingresar unidad de medida: ")
                            ingredientes.append(ingrediente)
                        except:
                            print("***** Valor tiene que ser un decimal *****")
                        else:
                            print("Ingrediente agregado con éxito")
                    comidas[indice]['ingredientes'] = ingredientes
            case 5:
                print("***** Agregar receta *****")
                nombre_comida = input("Ingrese el nombre de la comida: ")

                indice = 0
                encontrada = False
                for comida in comidas:
                    if nombre_comida == comida['nombre']:
                        print(mostrar_comida(comida))
                        encontrada = True
                    if not encontrada:
                        indice += 1
                if not encontrada:
                    print("Comida no encontrada")
                else:
                    print('***** Para salir debe ingresar la palabra "salir" en la descripcion del paso')
                    
                    pasos = []
                    ingresar = True
                    while(ingresar):
                        descripcion = input("Descripcion: ")

                        if descripcion == "Salir":
                            ingresar = False
                            continue;
                        else:
                            pasos.append(descripcion)
                    comidas[indice]['receta'] = pasos
            case 6:
                print("...Saliendo...")
                seguir = False
            case default:
                print("Opcion no valida")

print(comidas)