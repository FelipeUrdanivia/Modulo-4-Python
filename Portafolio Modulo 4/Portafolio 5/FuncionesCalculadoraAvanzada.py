def bienvenida():
    print("Bienvenido a Calculadora Interactiva")
    nombre = input("Escribe tu nombre: ")
    print("Hola "+nombre+" ¿Que deseas hacer?")
    return nombre

def opcion_menu():
    opcion = -1
    while opcion < 0 or opcion > 5:
        try:
            print("--------------------------------------------------")
            print("Acciones disponibles:")
            print("  1. Sumar")
            print("  2. Restar")
            print("  3. Multiplicar")
            print("  4. Dividir")
            print("  5. Potencia")
            print("  0. Salir")
            print("--------------------------------------------------")
            opcion = int(input("Ingrese una opcion entre 0 y 5: "))
        except ValueError:
            print("Por favor ingrese un valor numerico")
    return opcion

def suma():
    while True:
        try:
            n1 = float(input("Ingrese primer numero: "))
            n2 = float(input("Ingrese segundo numero: "))
            break
        except ValueError:
            print("Ingrese un valor numerico.")
    suma = n1 + n2
    return suma

def resta():
    while True:
        try:
            n1 = float(input("Ingrese primer numero: "))
            n2 = float(input("Ingrese segundo numero: "))
            break
        except ValueError:
            print("Ingrese un valor numerico.")
    resta = n1 - n2
    return resta

def multiplicacion():
    while True:
        try:
            n1 = float(input("Ingrese primer numero: "))
            n2 = float(input("Ingrese segundo numero: "))
            break
        except ValueError:
            print("Ingrese un valor numerico.")
    try:
        multi = n1 * n2
        return multi
    except OverflowError:
        print("Numero demasiado grande")
        return "Demasiado grande"

def division():
    try:
        while True:
            try:
                n1 = float(input("Ingrese primer numero: "))
                n2 = float(input("Ingrese segundo numero: "))
                break
            except ValueError:
                print("Ingrese un valor numerico.")
        divi = n1 / n2
        return divi
    except ZeroDivisionError:
        print("No se puede realizar división por cero")
        return "No existe"

def potencia():
    while True:
        try:
            n1 = float(input("Ingrese primer numero: "))
            n2 = float(input("Ingrese valor de la potencia: "))
            break
        except ValueError:
            print("Ingrese un valor numerico.")
    try:
        potencia = n1 ** n2
        return potencia
    except OverflowError:
        print("Numero demasiado grande")
        return "Demasiado grande"