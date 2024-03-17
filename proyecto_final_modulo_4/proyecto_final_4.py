class Automovil:
    def __init__(self,color,marca,modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    def get_velocidad(self):
        return self.velocidad
    def acelerar(self):
        self.velocidad += 10
    def frenar(self):
        if self.velocidad >= 5:
            self.velocidad -= 5
        else:
            print("El automovil está detenido")

auto1 = Automovil("Rojo","Nissan","SuperAuto")
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.acelerar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.acelerar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.acelerar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()
print(f"La velocidad del automovil es {auto1.get_velocidad()} km/h")
auto1.frenar()