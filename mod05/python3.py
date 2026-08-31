pienin = None
suurin = None

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break
    numero = float(luku)

    if pienin is None:
        pienin = numero
        suurin = numero
    else: 
        if numero < pienin:
            pienin = numero
        if numero > suurin:
            suurin = numero
   
  
        print(f"Pienin luku:", pienin)
        print(f"Suurin luku:", suurin)
    