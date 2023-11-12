#Programa de una Empresa de Aseo y Mantenimientos

def mostrar_contratos(contrato, estado):
    return f"Nombre del Empleado: {contrato['empleado']}, Lugar de Aseo: {contrato['area']}, Nombre del Cliente: {contrato['cliente']}, Identidad: {contrato['id']}, Precio de Contrato: {contrato['precio']}, Estado: {estado}"

def estado(estado):
    validar_estado = ["En espera", "En proceso", "Finalizado"]
    if estado in validar_estado:
        return estado
    else:
        return "Estado no válido"

contratos = []
contador = 0
opcion = 0
seguir = True

while(seguir):
    try:
        print("\n****** Menu *******")
        print("1. Agregar Contrato")
        print("2. Ver Contrato")
        print("3. Ver Contratos")
        print("4. Ver Contrato por Estado")
        print("5. Modificar estado")
        print("6. Salir")
        opcion = int(input("Seleccione una opción:"))
    except:
        print("Opcion no válida")
    else:
        match(opcion):
            case 1:
                contrato = {}
                print("**** Agregar Contrato ****")
                contrato['empleado'] = input("Ingrese nombre del empleado: ")
                contrato['area'] = float(input("Ingrese tamaño del lugar de trabajo: "))
                contrato['cliente'] = input("Ingrese nombre completo de Cliente: ")
                contrato['id'] = int(input("Ingrese identidad de Cliente: "))
                contrato['precio'] = float(input("Ingrese precio del contrato: "))
                ingresar_estado = input("Ingrese estado del contrato: ")
                estado_validado = estado(ingresar_estado)
                contrato['estado'] = estado_validado
                contratos.append(contrato)
                print("---- Contrato ingresado con éxito --------")
            case 2:
                print("**** Ver Contrato ****")
                nombre_contrato = input("Ingrese nombre del cliente: ")
                encontrado = False
                for contrato in contratos:
                    if nombre_contrato == contrato['cliente']:
                        print(mostrar_contratos(contrato, contrato['estado']))
                        encontrado = True
                if not encontrado:
                    print("Contrado no encontrado")
            case 3:
                print("***** Ver contratos ******")
                
                for contrato in contratos:
                    print(mostrar_contratos(contrato, contrato['estado']))
            case 4:
                print("**** Ver contrato por estado ****")
                estado_contrato = input("Ingrese estado de contrato: ")
                encontrado = False
                for contrato in contratos:
                    if estado(contrato['estado']) == estado_contrato:
                        print(mostrar_contratos(contrato, contrato['estado']))    
                        encontrado = True
                if not encontrado:
                    print("Contrato no encontrado por el tipo de estado")
            case 5:
                print("***Cambiar estado del contrato ****")
                nombre_cliente = input("Ingrese estado de contrato: ")
                encontrado = False
                for contrato in contratos:
                    if nombre_cliente == contrato['cliente']:
                        print(mostrar_contratos(contrato, contrato['estado']))
                        ingresar_estado = input("Ingrese nuevo estado del contrato: ")
                        estado_validado = estado(ingresar_estado)
                        contrato['estado'] = estado_validado
                        print("----Estado del contrato modificado con éxito. ----")
                        encontrado = True
                if not encontrado:
                    print("Contrato por estado no encontrado")
            case 6:
                print("Saliendo....")
                seguir = False
            case default:
                print("Opcion no válida")