print("Cálculo del promedio de notas de un curso leyendo desde archivo txt")
archivo = open("registro_notas.txt","r")
infoArchivo = []
linea = archivo.readline().rstrip().split(" ")
while len(linea) == 2:
        infoArchivo.append(linea)
        linea = archivo.readline().rstrip().split(" ")
archivo.close()
suma = 0
for linea in infoArchivo:
        print(f"La nota de {linea[0]} fue {linea[1]}")
        suma += float(linea[1])
promedio = suma / len(infoArchivo)
print(f"El promedio del curso fue {promedio}")