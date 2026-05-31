class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        print("Guau")


class Gato(Animal):
    def sonido(self):
        print("Miau")


animales = [Perro("Firulais"), Gato("Michi")]

for a in animales:
    a.sonido()
