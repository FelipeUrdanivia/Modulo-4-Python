class Escuela:
    def __init__ (self,nombre,pais,ciudad,subvencion):
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.subvencion = subvencion
class Personas:
    def __init__(self,nombre,rut,edad):
        self.nombre = nombre
        self.rut = rut
        self.edad = edad
    def asistir(self,escuela):
        print(f"{self.nombre} asiste a la escuela {escuela}")
class Profesores(Personas):
    def __init__(self, nombre, rut, edad,asignatura):
        super().__init__(nombre, rut, edad)
        self.asignatura = asignatura
    def presentarse (self):
        print(f"Hola soy {self.nombre} profesor del curso {self.asignatura}")
    def pasarLista (self):
        print(f"El profesor {self.nombre} pasa lista en la clase de {self.asignatura}")
    def enseñarContenidos(self,contenidos):
        print(f"El profesor {self.nombre} enseña contenidos de {self.asignatura}")
        for contenido in contenidos:
            print(contenido)
    def evaluarContenidos(self):
        print(f"El profesor {self.nombre} evalua los contenidos de {self.asignatura}")
class Alumnos(Personas):
    def __init__(self, nombre, rut, edad,curso,promedio,asistencia):
        super().__init__(nombre, rut, edad)
        self.curso = curso
        self.promedio = promedio
        self.asistencia = asistencia
    def presentarse (self):
        print(f"Hola soy {self.nombre} alumno del curso {self.curso}")
    def decirPresente (self):
        print(f"{self.nombre} dice presente")
    def estudiar(self):
        print(f"{self.nombre} está estudiando")
    def responderPrueba(self):
        print(f"{self.nombre} responde la prueba")
class Cursos():
    def __init__(self,nombre):
        self.nombre = nombre
    def crearLista(self,lista):
        self.listaAlumnos = lista
class Asignaturas():
    def __init__(self,nombre):
        self.nombre = nombre
    def crearContenidos(self,contenidos):
        self.contenidos = contenidos
#Creo Curso
cursoPython = Cursos("Python Mañana")
#Creo Contenidos y Asignatura
contenidosPython = ["Tipos Variables","Diagrama de clases"]
python = Asignaturas("Python")
python.crearContenidos(contenidosPython)
#Creo Escuela
escuelita = Escuela("La Escuelita","Chile","Santiago","Subvencionada")
#Creo Alumnos
felipe = Alumnos("Felipe","12.552.043-k",30,cursoPython.nombre,7.0,95.0)
jorge = Alumnos("Jorge","14.071.372-k",25,cursoPython.nombre,7.0,95.0)
sebastian = Alumnos("Sebastian","19.642.874-k",33,cursoPython.nombre,7.0,95.0)
catalina = Alumnos("Catalina","27.478.107-k",23,cursoPython.nombre,7.0,95.0)
#Creo Profesor
bastian = Profesores("Bastian","15.938.398-k",32,python.nombre)
#Lista de alumnos
alumnosPython = [felipe,jorge,sebastian,catalina]
cursoPython.crearLista(alumnosPython)
#Llamado a metodos
print("---------------------------------------")
print("Profesor y alumnos se presentan")
bastian.presentarse()
for alumno in cursoPython.listaAlumnos:
    alumno.presentarse()
print("---------------------------------------")
bastian.pasarLista()
for alumno in cursoPython.listaAlumnos:
    alumno.decirPresente()
print("---------------------------------------")
bastian.enseñarContenidos(python.contenidos)
print("---------------------------------------")
print("Alumnos estudian contenidos")
for alumno in cursoPython.listaAlumnos:
    alumno.estudiar()
print("---------------------------------------")
bastian.evaluarContenidos()
print("---------------------------------------")
print("Alumnos rinden prueba")
for alumno in cursoPython.listaAlumnos:
    alumno.responderPrueba()
print("---------------------------------------")
print("Termina la clase")
print("---------------------------------------")