class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ficha: {self.ficha}")
        print(f"Promedio: {self.promedio}")

    def aprobo(self):
        return self.promedio >= 3.0

estudiante1 = Estudiante("Ana Gómez", "2873610", 2.8)
estudiante2 = Estudiante("Carlos Pérez", "2873610", 4.1)

print("Perfil Estudiante 1 ")
estudiante1.mostrar_perfil()
print(f"¿Aprobó?: {estudiante1.aprobo()}\n")

print("Perfil Estudiante 2 ")
estudiante2.mostrar_perfil()
print(f"¿Aprobó?: {estudiante2.aprobo()}")