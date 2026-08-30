x = int(input("Anna luku: "))

if x <= 10:
    print(f"Lukusi {x} oli pieninempi kuin 10")
elif x >= 20:
    print(f"Lukusi {x} oli ja suurempi kuin 20.")
elif x > 10 and x < 20:
    print(f"Lukusi {x} on 10 ja 20 väliltä.")
