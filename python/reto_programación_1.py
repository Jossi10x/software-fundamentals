import random

dado = int(random.randint(1,6))

if dado % 2 == 0:
  print(f"El resultado del dado es: {dado}\nEl número es par")
else:
 print(f"El resultado del dado es: {dado}\nEl número es impar")
