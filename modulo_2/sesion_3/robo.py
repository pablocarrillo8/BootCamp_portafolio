# Clases

class Estudiante:

    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def presentarse(self):
        return f"Hola {self.nombre} !"

estudiante1 = Estudiante("Paula", True)
print(estudiante1.presentarse())