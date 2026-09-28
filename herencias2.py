class usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print(f"hola soy {self.nombre}, y mi apellido es {self.apellido}")


class aprendiz(usuario):
    pass


ap = aprendiz("luis", "lopez")
ap.saludar()