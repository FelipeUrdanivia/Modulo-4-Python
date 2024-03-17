class Empleado:
    def __init__(self,nombre,rut,edad,departamento):
        self.nombre = nombre
        self.rut = rut
        self.edad = edad
        self.departamento = departamento
class Departamento:
    def __init__(self,nombre):
        self.nombre = nombre
class Desarrollador(Empleado):
    def __init__(self, nombre, rut, edad, departamento):
        super().__init__(nombre, rut, edad, departamento)
    def trabajar(self):
        print(f"El Desarrollador {self.nombre} está haciendo una aplicación")
class Gerente(Empleado):
    def __init__(self, nombre, rut, edad, departamento):
        super().__init__(nombre, rut, edad, departamento) 
    def trabajar(self):
        print(f"El Gerente {self.nombre} está dirigiendo a su equipo")

departamento1 = Departamento("Finanzas")
departamento2 = Departamento("TI")
empleado1 = Desarrollador("Juan","12.123.456-3",45,departamento1)
empleado2 = Desarrollador("Francisco","14.654.234-6",35,departamento2)
empleado3 = Gerente("Claudio","14.654.345-8",30,departamento1)
empleado1.trabajar()
empleado2.trabajar()
empleado3.trabajar()
print(f"{empleado1.nombre} - Departamento: {empleado1.departamento.nombre}")
print(f"{empleado2.nombre} - Departamento: {empleado2.departamento.nombre}")
print(f"{empleado3.nombre} - Departamento: {empleado3.departamento.nombre}")                             