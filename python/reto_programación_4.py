import random

contador = 0

while True:
  contador = contador + 1
  dado1 = random.randint(1,6)
  dado2 = random.randint(1,6)
  print(f"Lanzamiento {contador}: Salió {dado1} y {dado2}")

  if dado1 == 6 and dado2 == 6:
    print(f"Sacaste un par de 6")
    break