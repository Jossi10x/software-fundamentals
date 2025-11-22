import random

def Contador(num_intentos):
  cont_pares = 0
  cont_impares = 0
  for i in range(1, num_intentos + 1):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    if dado1 % 2 == 0 and dado2 % 2 == 0:
      cont_pares += 1
    else:
      cont_impares += 1
  print(f"El número de lanzamientos pares fue de: {cont_pares}\nEl número de lanzamientos impares fue de: {cont_impares}")

num_intentos = int(input("Cuantos lanzamientos quieres realizar (Máximo 100): "))
if num_intentos > 0 and num_intentos <= 100:
  Contador(num_intentos)
else:
  print(f"El número de intentos no es válido!")