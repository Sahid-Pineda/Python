while True:
    print("\nOperacion que desea realizar: \n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
    entrada = int(input("==>"))

    try:
        ent == int(entrada)

        if ent == 1:
            print("Suma\n")
            n1 = float(input("Ingrese un valor para n1= "))
            n2 = float(input("ingrese un valor para n2= "))
            resultado = n1 + n2
            print("La suma es: ", resultado)
        elif ent == 2:
            print("Resta\n")
            n1 = float(input("Ingrese un valor para n1= "))
            n2 = float(input("ingrese un valor para n2= "))
            resultado = n1 - n2
            print("La resta es: ",resultado)
        elif ent == 3:
            print("Multiplicación\n")
            n1 = float(input("Ingrese un valor para n1= "))
            n2 = float(input("ingrese un valor para n2= "))
            resultado = n1 *n2
            print("El producto es: ", resultado)
        elif ent == 4:
            print("División\n")
            n1 = float(input("Ingrese un valor para n1= "))
            n2 = float(input("ingrese un valor para n2= "))
        
            if n2 == 0:
                print("No se puede dividir entre 0")
            else :
                resultado = n1 / n2
                print("La división es: ", resultado)
        elif ent == 5:
            print("Salir")
            break
        else :
            print("Opción sin programar")
    except ValueError:
        print("Ingresa un numero válido.")