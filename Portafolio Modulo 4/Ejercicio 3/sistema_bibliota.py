class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.disponibles = []
        self.clientes = []
        self.faltantes = []
    def ingresar_libros(self,id,titulo,autor):
        self.disponibles.append(Libros(id,titulo,autor))
    def registrar_cliente(self,id,nombre,rut,fNacimiento):
        self.clientes.append(self.Cliente(id,nombre,rut,fNacimiento))
    def prestar_libros(self,id,titulo):
        i = 0
        for cliente in self.clientes:
            if cliente.id == id:
                j = 0
                for libro in self.disponibles:
                    if libro.titulo == titulo:
                        cliente.prestados.append(libro)
                        self.disponibles.remove(libro)
                        self.faltantes.append(libro)
                        break
                    j += 1
                    if j == len(self.disponibles):
                        print("Libro no disponible")
                break
            i += 1
            if i == len(self.clientes):
                print("ID cliente no registrada")
    def recibir_libros(self,idCliente,idLibro):
        i = 0
        for cliente in self.clientes:
            if cliente.id == idCliente:
                j = 0
                for libro in cliente.prestados:
                    if libro.id == idLibro:
                        cliente.prestados.remove(libro)
                        self.disponibles.append(libro)
                        self.faltantes.remove(libro)
                        break
                    j += 1
                    if j == len(cliente.prestados):
                        print("ID libro no encontrada")
                break
            i += 1
            if i == len(self.clientes):
                print("ID cliente no registrada")
    def ver_disponibles(self):
        for libro in self.disponibles:
            print(f"ID: {libro.id} - {libro.titulo} - {libro.autor.nombre}")
    def ver_faltantes(self):
        for libro in self.faltantes:
            print(f"ID: {libro.id} - {libro.titulo} - {libro.autor.nombre}")
    def ver_clientes(self):
        for cliente in self.clientes:
            print(f"ID: {cliente.id} - {cliente.nombre}")
    class Cliente():
        def __init__(self,id,nombre,rut,fNacimiento):
            self.id = id
            self.nombre = nombre
            self.rut = rut
            self.fNacimiento = fNacimiento
            self.prestados = []
        def ver_pendientes(self):
            print(f"Libros pendientes de ID: {self.id} - {self.nombre}")
            for libro in self.prestados:
                print(f"ID: {libro.id} - {libro.titulo} - {libro.autor.nombre}")
class Autor:
    def __init__(self,nombre,fNacimiento):
        self.nombre = nombre
        self.fNacimiento = fNacimiento
class Libros:
    def __init__(self,id,titulo,autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

autor1 = Autor("Herman Melville","17/08/2001")
autor2 = Autor("Miguel de Cervantes","1/02/1985")
autor3 = Autor("Marcela Paz","17/08/1974")
libreria = Biblioteca("Libreria")
libreria.ingresar_libros("1","Moby Dick",autor1)
libreria.ingresar_libros("2","Taipi",autor1)
libreria.ingresar_libros("3","Don Quijote de la Mancha",autor2)
libreria.ingresar_libros("4","Papelucho",autor3)
libreria.registrar_cliente("1","Juanito","19.234.554-1","17/08/2001")
libreria.registrar_cliente("2","Claudio","13.234.354-5","17/08/1974")
libreria.registrar_cliente("3","Fernando","15.234.854-2","17/08/1962")
libreria.registrar_cliente("4","Josefa","18.234.654-4","17/08/1943")
libreria.registrar_cliente("5","Camila","12.237.534-k","1/02/1985")
print("------------------------------------------------------------")
print("Clientes de la Biblioteca: ")
libreria.ver_clientes()
print("------------------------------------------------------------")
print("Libros disponibles de la Biblioteca: ")
libreria.ver_disponibles()
print("------------------------------------------------------------")
print("Se prestan libros a dos clientes")
libreria.prestar_libros("1","Moby Dick")
libreria.prestar_libros("5","Papelucho")
print("------------------------------------------------------------")
print("Libros disponibles de la Biblioteca: ")
libreria.ver_disponibles()
print("------------------------------------------------------------")
print("Libros Faltantes de la Biblioteca: ")
libreria.ver_faltantes()
print("------------------------------------------------------------")
libreria.clientes[0].ver_pendientes()
print("------------------------------------------------------------")
libreria.clientes[4].ver_pendientes()
print("------------------------------------------------------------")
print("Camila devuelve el libro que pidió prestado")
libreria.recibir_libros("5","4")
print("------------------------------------------------------------")
print("Libros disponibles de la Biblioteca: ")
libreria.ver_disponibles()
print("------------------------------------------------------------")
print("Libros Faltantes de la Biblioteca: ")
libreria.ver_faltantes()
print("------------------------------------------------------------")