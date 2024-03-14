class Pelicula:
    def __init__(self,titulo,director,genero,duracion):
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion
    def info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Director: {self.director}")
        print(f"Genero: {self.genero}")
        print(f"Duracion: {self.duracion}")
        print("--------------------------------------------------")
listaPeliculas = []
i= 1
while i < 6:
    print(f"Ingresando informacion pelicula numero {i}")
    titulo = input(f"Titulo pelicula {i}: ")
    director = input(f"Director pelicula {i}: ")
    genero = input(f"Genero pelicula {i}: ")
    duracion = input(f"Duracion pelicula {i}: ")
    print("--------------------------------------------------")
    listaPeliculas.append(Pelicula(titulo,director,genero,duracion))
    i += 1
for pelicula in listaPeliculas:
    pelicula.info()