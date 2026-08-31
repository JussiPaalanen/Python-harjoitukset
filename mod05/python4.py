import random

x = random.randint(1, 10)


while True:
    y = int(input("Arvaa luku: "))

    if y < x:
        print(f"Liian pieni arvaus. ")
    elif y > x:
        print(f"Liian suuri arvaus. ")
    elif y == x:
        print(f"Oikein!")