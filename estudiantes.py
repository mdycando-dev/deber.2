class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__nota = 0

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def mostrar(self):
        pass


class Estudiante(Persona):
    def mostrar(self):
        print(f"Estudiante: {self.nombre}")


class Becado(Persona):
    def mostrar(self):
        print(f"Becado: {self.nombre}")


personas = [Estudiante("Ana"), Becado("Pedro")]

for p in personas:
    p.mostrar()
