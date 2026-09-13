list1 = []

while True:
    nimi = input(f"Anna nimi: ")
    if nimi == "":
        break
    elif nimi in list1:
        print(f"Aiemmin annettu nimi")
    else:
        print(f"Uusi nimi")
        list1.append(nimi)
        continue

for i in list1:
    print(f"{i}")
