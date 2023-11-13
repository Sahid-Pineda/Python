from abc import ABC, abstractmethod
import math

pi = math.pi

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(Figura):
    lado = None

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado
    
class Rectangulo(Figura):
    largo = None
    ancho = None

    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho
    
class Circulo(Figura):
    radio = None

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return pi * math.pow(self.radio, 2)

tipo = 0    
opcion = 0
seguir = True

while(seguir):
    try:
        print("\n**** Menú ****")
        print("1. Calcular área de una Figura")
        print("2. Salir")
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opción no válida")
    else:
        match opcion:
            case 1:
                try:
                    print("\nCalcular Área")
                    print("Tipo\n   1- Cuadrado\n   2- Rectangulo\n   3- Circulo")
                    tipo = int(input("Seleccione una opción: "))
                    match tipo:
                        case 1:
                                print("Cuadrado")
                                lado = float(input("Lado: "))
                                cuadrado = Cuadrado(lado)
                                print("Área del Cuadrado: ", cuadrado.calcular_area())
                        case 2:
                                print("Rectangulo")
                                largo = float(input("Largo: "))
                                ancho = float(input("Ancho: "))
                                rectangulo = Rectangulo(largo, ancho)
                                print("Área del Rectángulo: ", rectangulo.calcular_area())
                        case 3:
                                print("Circulo")
                                radio = float(input("Radio: "))
                                circulo = Circulo(radio)
                                print("Área del Circulo: ", circulo.calcular_area())
                        case default:
                            print("Opcion no válida")
                except:
                    print("Opcion no válida")       
            case 2:
                print("Saliendo...")
                seguir = False
            case default:
                print("Opcion no válida")