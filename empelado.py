class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__salario = 0

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def mostrar_datos(self):
        pass


class Profesor(Empleado):
    def mostrar_datos(self):
        print(f"Profesor: {self.nombre}")


class Secretario(Empleado):
    def mostrar_datos(self):
        print(f"Secretario: {self.nombre}")


empleados = [Profesor("Carlos"), Secretario("Luis")]

for e in empleados:
    e.mostrar_datos()
