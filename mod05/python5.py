oikea_käyttäjätunnus = "python"
oikea_salasana = "rules"
kerrat = 0

while kerrat < 5:

    x = input("Anna käyttäjä tunnus: ")
    y = input("Anna salasana: ")

    if x == oikea_käyttäjätunnus and y == oikea_salasana:
        print(f"Tervetuloa!")
        break

    kerrat += 1
else:
    print(f"Pääsy evätty.")

