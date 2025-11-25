import random

suma_total = 0
total_tiros = 0
cant_pares = 0 
cant_impares = 0 
continuar = 1

while continuar == 1:
  print("Bienvenido!\n1.Lanzar\n2.Salir")
  desicion = int(input())
  if desicion == 1:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma_lanzamiento = dado1 + dado2
    suma_total = suma_total + suma_lanzamiento
    total_tiros += 1
    if dado1 % 2 == 0 and dado2 % 2 == 0:
      cant_pares += 1
    else:
      cant_impares += 1
  else:
    print(f"Numero de intentos: {total_tiros}\nPuntaje total: {suma_total}\nCantidad de pares: {cant_pares}\nCantidad de impares: {cant_impares}")
    continuar = 2