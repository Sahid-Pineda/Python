#Clase Padre
class Contrato:
    def __init__(self, empleado, area, cliente, identidad, precio, estado):
        self.empleado = empleado
        self.area = area
        self.cliente = cliente
        self.identidad = identidad
        self.precio = precio
        self.estado = estado

    def __str__(self):
        return f"Empleado: {self.empleado}, Área de trabajo: {self.area}, Cliente: {self.cliente}, Identidad: {self.identidad}, Precio: {self.precio}, Estado: {self.estado}"
    
#Clase Hija
class EmpresaAseo:
    def __init__(self):
        self.contratos = []

    def agregar_contrato(self, contrato):
        self.contratos.append(contrato)

    def mostrar_contratos(self):
        for contrato in self.contratos:
            print(contrato)
    
    def buscar_contrato_por_cliente(self, nombre_cliente):
        for contrato in self.contratos:
            if contrato.cliente == nombre_cliente:
                print(contrato)

    def cambiar_estado(self, nombre_cliente, nuevo_estado):
        for contrato in self.contratos:
            if contrato.cliente == nombre_cliente:
                contrato.estado = nuevo_estado
                print(f"Estado del contrato de {nombre_cliente} cambiado a {nuevo_estado}")
                break

mi_empresa = EmpresaAseo()

contrato1 = Contrato("Daniel Pineda", 100, "Claudia Rodriguez", 23244243, 3000, "En proceso")
contrato2 = Contrato("Rosalia Rodriguez", 100, "Christian Pineda", 32345233, 2500, "En espera")
mi_empresa.agregar_contrato(contrato1)
mi_empresa.agregar_contrato(contrato2)

print("Contratos: ")
mi_empresa.mostrar_contratos()

print("\nBuscar contrato por cliente: ")
mi_empresa.buscar_contrato_por_cliente("Christian Pineda")

mi_empresa.cambiar_estado("Christian Pineda", "Finalizado")

print("\nContratos Actualizados: ")
mi_empresa.mostrar_contratos()