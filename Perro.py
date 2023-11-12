class Perro:
    nombre= None
    raza = None
    peso = None

    #Constructor
    def __init__(self, nombre, raza, peso, docil = True, peligroso = False, disponible_para_adoptar = True):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
    
    #Destrutor
    def __del__(self):
        print("Objeto destruido")

class Albergue:
    def __init__(self):
        self.perros = []

    def ingresar_perro(self, perro):
        self.perros.append(perro)
    
    def ver_todos_los_perros(self):
        for perro in self.perros:
            print(f"Nombe: {perro.nombre}, Raza: {perro.raza}, Peso: {perro.peso}, Docil: {perro.docil}, Peligroso: {perro.peligroso}, Disponible para adoptar: {perro.dispobible_para_adoptar}")

    def ver_perro_especifico(self, nombre):
        encontrado = False
        for perro in self.perros:
            if perro.nombre == nombre:
                print(f"Nombe: {perro.nombre}, Raza: {perro.raza}, Peso: {perro.peso}, Docil: {perro.docil}, Peligroso: {perro.peligroso}, Disponible para adoptar: {perro.dispobible_para_adoptar}")
                return
        print(f"No se encontro un perro con el nombre {nombre}")

    def cambiar_estado(self, nombre):
        for perro in self.perros:
            if perro.nombre == nombre:
                perro.disponible_para_adopcion = not perro.disponible_para_adopcion
                print(f"El estado de adopcion de {nombre} ha sido cambiado a {perro.dispobile_para_adopcion}.")
                return
        print(f"No se encontró un perro con el nombre {nombre}")

    