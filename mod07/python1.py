import random

def f():
    while True:
        luku = random.randint(1, 6)
        if luku != 6:
            print(f"{luku}")
        else: 
            break
    print(f"{luku}")
    

f()