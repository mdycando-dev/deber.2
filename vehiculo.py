class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.__velocidad = 0

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def mostrar_info(self):
        pass


class Auto(Vehiculo):
    def mostrar_info(self):
        print(f"Auto {self.marca} - {self.get_velocidad()} km/h")


class Moto(Vehiculo):
    def mostrar_info(self):
        print(f"Moto {self.marca} - {self.get_velocidad()} km/h")


vehiculos = [Auto("Toyota"), Moto("Yamaha")]

for v in vehiculos:
    v.set_velocidad(100)
    v.mostrar_info()
