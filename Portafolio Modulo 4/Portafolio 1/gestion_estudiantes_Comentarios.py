#Creacion de la clase Estudiante
class Estudiante ():
    #Iniciacion de los atributos clase estudiante
    def __init__(self,nombre,edad,calificaciones):
        #Igualar todas las self.variable a su respectiva variable
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
    #Creacion del metodo calcularPromedio
    #Siempre lleva self, mantiene toda la clase conectada
    def calcularPromedio(self):
        #Creo una variable suma que guardará todas las notas
        suma = 0
        #Ciclo for para recorrer self.calificaciones
        #self.calificaciones es la lista que guarda las notas
        for nota in self.calificaciones:
            #Por cada vuelta suma agrega una nota
            suma = suma + nota
        #cantidad es la cantidad de notas que tiene la lista
        cantidad = len(self.calificaciones)
        promedio = suma / cantidad
        #Guardo promedio en self.promedio
        #Esto se transformará en un atributo de la clase
        #Así podré acceder a él en el futuro
        self.promedio = promedio
#Creo una lista con las notas de Felipe y la guardo en notasFelipe
notasFelipe = [5,6,7,4]
#Creo el objeto estudiante 1
estudiante1 = Estudiante("Felipe",30,notasFelipe)
#Creo el objeto estudiante 2
#En este caso entrego la lista de notas directamente
estudiante2 = Estudiante("Felipe",20,[3,4,2,1])
#Llamo a los metodos calcular promedio para cada objeto
#Sin llamar al metodo este no se ejecutará
estudiante1.calcularPromedio()
estudiante2.calcularPromedio()
#Genero un print para entregar la información
#Accediendo a distintos atributos de cada objeto
#Los estudiantes son objetos creados con la clase Estudiante
print(f"El promedio de {estudiante1.nombre} es {estudiante1.promedio}")
print(f"El promedio de {estudiante2.nombre} es {estudiante2.promedio}")