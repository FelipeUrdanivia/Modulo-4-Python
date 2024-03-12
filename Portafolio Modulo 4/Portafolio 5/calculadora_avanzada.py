import FuncionesCalculadoraAvanzada as cal

nombre = cal.bienvenida()

opcion = 1
while opcion != 0:
    opcion = cal.opcion_menu()
    if opcion == 1:
        resultado = cal.suma()
        print("El resultado de la suma es: "+str(resultado))
    elif opcion == 2:
        resultado = cal.resta()
        print("El resultado de la resta es: "+str(resultado))
    elif opcion == 3:
        resultado = cal.multiplicacion()
        print("El resultado de la multiplicacion es: "+str(resultado))
    elif opcion == 4:
        resultado = cal.division()
        print("El resultado de la division es: "+str(resultado))
    elif opcion == 5:
        resultado = cal.potencia()
        print("El resultado de la potencia es: "+str(resultado))
    elif opcion == 0:
        print("Has decidido salir de tu calculadora interactiva, hasta luego "+ nombre + ".")