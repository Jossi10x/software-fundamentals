import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

if dado1 % 2 == 0:
    print("El dado 1 es par")
else:
    print("El dado 1 es impar")

if dado2 % 2 == 0:
    print("El dado 2 es par")
else:
    print("El dado 2 es impar")

if dado1 == dado2:
    print("Sacaste un par! You win!")
else:
    print("Game over!")
