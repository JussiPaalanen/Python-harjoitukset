import random

def f(tahko):
    while True:
        luku = random.randint(0, tahko)
        if luku != tahko:
            print(f"{luku}")
            continue
        else: 
            break
    print(f"{luku}")

f(21)