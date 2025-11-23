num_usuario = int(input("Ingrese un número entero (positivo o negativo): "))

if num_usuario > 0:
    if num_usuario % 2 == 0:
        print("El número entero es par positivo")
    else:
        print("El número entero es impar positivo")
else:
    if num_usuario % 2 == 0:
        print("El número entero es par negativo")
    else:
        print("El número entero es impar negativo")