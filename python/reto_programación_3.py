import random

contadores = []

num_intentos = int(input("Cuantas veces quieres lanzar el dado (Máximo 100 veces): "))

for i in range(6):
  contadores.append(0)

if num_intentos > 0 and num_intentos <= 100:
  for i in range(1, num_intentos+1):
    dado = random.randint(1,6)
    contadores[dado - 1] += 1
    print(f"Dado {i}: {dado}")

  for i in range(6):
      cara = i + 1
      print(f"Dado {cara}: salió {contadores[i]} veces")

else:
  print("El número de intentos no es válido!")