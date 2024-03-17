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
        def crearCuenta(self,numero):
            self.cuentas.append(self.Cuenta(self.nombre,numero))
        def depositar(self,cuenta,monto):
            cuenta.saldo += monto
        def retirar (self,cuenta,monto):
            if monto <= cuenta.saldo:
                cuenta.saldo -= monto
            else:
                print("Saldo Insuficiente")
        def transferir (self,cuenta1,cuenta2,monto):
            if monto <= cuenta1.saldo:
                cuenta1.saldo -= monto
                cuenta2.saldo += monto
            else:
                print("Saldo Insuficiente")
        class Cuenta:
            def __init__(self,nombre,numero):
                self.titular = nombre
                self.numero = numero
                self.saldo = 0
#Abrir banco
santander = Banco("Santander")
print("Ingrese datos primer cliente")
santander.agregarCliente()
print("--------------------------------")
print("Ingrese datos segundo cliente")
santander.agregarCliente()
print("--------------------------------")
#Creando cuenta cliente 1
santander.clientes[0].crearCuenta("1234")
#Creando cuenta cliente 2
santander.clientes[1].crearCuenta("5678")
#Deposito a cuenta cliente 1
santander.clientes[0].depositar(santander.clientes[0].cuentas[0],2000)
print("Saldo en cuenta 1 de cliente 1")
print(santander.clientes[0].cuentas[0].saldo)
print("--------------------------------")
#Transferencia de cliente 1 a cliente 2
santander.clientes[0].transferir(santander.clientes[0].cuentas[0],santander.clientes[1].cuentas[0],1000)
print("Saldo en cuenta 1 de cliente 2")
print(santander.clientes[1].cuentas[0].saldo)
print("--------------------------------")