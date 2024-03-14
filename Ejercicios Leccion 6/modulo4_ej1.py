class Automovil:
    def __init__(self,color,marca,modelo,puertas,patente):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas
        self.patente = patente
    def info(self):
        print(f"Caracteristicas del automovil patente {self.patente}")
        print(f"Color: {self.color}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cantidad puertas: {self.puertas}")
        print("--------------------------------------------------")
listaAutos = []
i= 1
while i < 6:
    print(f"Creacion automovil numero {i}")
    color = input(f"Color del automovil {i}: ")
    marca = input(f"Marca del automovil {i}: ")
    modelo = input(f"Modelo del automovil {i}: ")
    puertas = input(f"Número de puertas del automovil {i}: ")
    patente = input(f"Patente del automovil {i}: ")
    print("--------------------------------------------------")
    listaAutos.append(Automovil(color,marca,modelo,puertas,patente))
    i += 1
for auto in listaAutos:
    auto.info()