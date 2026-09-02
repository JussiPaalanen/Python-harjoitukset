import random

määrä = int(input("Arpakuutioiden määrä: "))

summa = 0

for i in range(määrä):
    silmäluku = random.randint(1, 6)
    summa += silmäluku

print(f"Arpakuutioiden summa on {summa}")