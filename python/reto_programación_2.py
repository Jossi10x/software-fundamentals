import random

suma = 0
num_intentos = int(input("Seleccione las veces para lanzar el dado (Máximo 10): "))
intentos = []

if num_intentos > 0 and num_intentos <= 10:
  for i in range(1, num_intentos + 1):
    dado = random.randint(1,6)
    intentos.append(dado)
    print(f"Dado {i}: {dado}")

  for i in range(num_intentos):
    suma = suma + intentos[i]
  print(f"El puntaje de sus lanzamientos es de ",suma)