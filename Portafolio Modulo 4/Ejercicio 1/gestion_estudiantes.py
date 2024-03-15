class Estudiante:
    def __init__(self,nombre,edad,calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
    def calcularPromedio(self):
        suma = 0
        for nota in self.calificaciones:
            suma = suma + nota
        cantidad = len(self.calificaciones)
        promedio = suma / cantidad
        self.promedio = promedio
notasFelipe = [5,6,7,4]
estudiante1 = Estudiante("Felipe",30,notasFelipe)
estudiante2 = Estudiante("Felipe",20,[3,4,2,1])
estudiante1.calcularPromedio()
estudiante2.calcularPromedio()
print(f"El promedio de {estudiante1.nombre} es {estudiante1.promedio}")
print(f"El promedio de {estudiante2.nombre} es {estudiante2.promedio}")