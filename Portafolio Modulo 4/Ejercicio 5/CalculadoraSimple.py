def validarDatos():
    while True:
        try:
            n1 = float(input("Ingrese primer numero: "))
            break
        except ValueError:
            print("Solo se aceptan valores numericos.")
    while True:
        try:
            n2 = float(input("Ingrese segundo numero: "))
            break
        except ValueError:
            print("Solo se aceptan valores numericos.")
    return (n1,n2)
while True:
    opcion = -1
    while opcion < 0 or opcion > 4:
        try:
            print("--------------------------------------------------")
            print("Acciones disponibles:")
            print("  1. Sumar")
            print("  2. Restar")
            print("  3. Multiplicar")
            print("  4. Dividir")
            print("  0. Salir")
            print("--------------------------------------------------")
            opcion = int(input("Ingrese numero correspondiente a la operacion: "))
        except ValueError:
            print("Solo se aceptan valores numericos")
    if opcion == 1:
        print("Realizando suma")
        (n1,n2) = validarDatos()
        suma = n1 + n2
        print(f"El resultado de la suma es: {suma}")
    elif opcion == 2:
        print("Realizando resta")
        (n1,n2) = validarDatos()
        resta = n1 - n2
        print(f"El resultado de la resta es: {resta}")
    elif opcion == 3:
        print("Realizando multiplicacion")
        (n1,n2) = validarDatos()
        multiplicacion = n1 * n2
        print(f"El resultado de la multiplicacion es: {multiplicacion}")
    elif opcion == 4:
        print("Realizando division")
        (n1,n2) = validarDatos()
        try:
            division = n1 / n2
            print(f"El resultado de la division es: {division}")
        except ZeroDivisionError:
            print("No se puede realizar division por cero")
    elif opcion == 0:
        print("Has decidido salir. Adios.")
        break