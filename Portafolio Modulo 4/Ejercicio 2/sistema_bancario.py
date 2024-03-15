class Banco:
    def __init__(self,nombre):
        self.nombre = nombre
        self.clientes = []
    def agregarCliente(self):
        self.clientes.append(self.Clientes())
    class Clientes:
        def __init__(self):
            self.nombre = input("Ingrese nombre cliente: ")
            self.rut = input("Ingrese rut cliente: ")
            self.cuentas = []
        def crearCuenta(self):
            self.cuentas.append(self.Cuenta(self.nombre))
        class Cuenta:
            def __init__(self,nombre):
                self.titular = nombre
                self.numero = "12345"
                self.saldo = 0
santander = Banco("Santander")
santander.agregarCliente()
santander.clientes[0].crearCuenta()
print(santander.clientes[0].cuentas[0].titular)