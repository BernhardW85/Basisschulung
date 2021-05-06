# loops / Schleifen

import random

# secret = 16
# guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
# if guess == secret:
#     print("Gratruliere - gewonnen. Es ist die Nummer 11")
# else:
#     print("Falsch... Die richtige Zahl war " + str(secret))

# secret = 16
# guess = 0
# while guess != secret:
#     guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
#     if guess == secret:
#         print("Gratruliere - gewonnen. Es ist die Nummer 11")
#     else:
#         print("Falsch... Die richtige Zahl war " + str(secret))

# secret = 18
# for x in range(3):
#     guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
#     if guess == secret:
#         print("Gratruliere - gewonnen. Es ist die Nummer 11")
#         break
#     else:
#         print("Falsch... Die richtige Zahl war NICHT " + str(guess))
#         print(x)
secret = random.randint(1,30)
while True:  # Endlos-Schleife --> break immer notwendig
    guess = int(input("Bitte Zahl raten (zwischen 1 und 30): "))
    if guess == secret:
        print("Gratruliere - gewonnen. Es ist die Nummer " + str(secret))
        break
    elif guess > secret:
        print("Falsch ... die gesuchte Zahl ist kleiner")
    elif guess < secret:
        print("Falsch... die gesuchte Zahl ist größer")
    else:
        print("Falsch... Die richtige Zahl war " + str(secret))
