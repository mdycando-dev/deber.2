class Electrodomestico:
    def __init__(self, marca):
        self.marca = marca
        self.__consumo = 0

    def get_consumo(self):
        return self.__consumo

    def set_consumo(self, consumo):
        self.__consumo = consumo

    def mostrar(self):
        pass


class Refrigeradora(Electrodomestico):
    def mostrar(self):
        print(f"Refrigeradora {self.marca}")


class Microondas(Electrodomestico):
    def mostrar(self):
        print(f"Microondas {self.marca}")


electros = [Refrigeradora("LG"), Microondas("Samsung")]

for e in electros:
    e.mostrar()
