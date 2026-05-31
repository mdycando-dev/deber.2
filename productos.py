class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__precio = 0

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def mostrar(self):
        pass


class Laptop(Producto):
    def mostrar(self):
        print(f"Laptop: {self.nombre}")


class Celular(Producto):
    def mostrar(self):
        print(f"Celular: {self.nombre}")


productos = [Laptop("Lenovo"), Celular("Samsung")]

for p in productos:
    p.mostrar()
