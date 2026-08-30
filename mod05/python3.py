pienin = None
suurin = None

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break
    numero = float(luku)

    if numero is None or numero < pienin:
        numero = pienin
    elif numero is None or numero > suurin:
        numero = suurin

  
        print(f"Pienin luku:", pienin)
        print(f"Suurin luku:", suurin)
    