nimi = input("Mikä on pelinimesi:\n")
ikä = int(input("Mikä on ikäsi:\n"))

print(f"{nimi}")
print(f"{ikä}")

while ikä > 12:
    print(f"Tervetuloa")
    break

    
else:
    print(f"Olet Alaikäinen")

def nayta_valikko():
    print("\n--- PÄÄVALIKKO ---")
    print("1. Peli1")
    print("2. Peli2")
    print("3. Peli3")
    print("0. Lopeta")

def main():
    while True:
        nayta_valikko()
        valinta = input("Valitse: ").strip()

        if valinta == "1":
            print(f"Ladataan peli1...")
            break
        elif valinta == "2":
            print(f"Ladataan peli2...")
            break
        elif valinta == "3":
            print(f"Ladataan peli3...")
            break
        elif valinta == "0":
            print(f"Lopetetaan.")
            break
        else:
            print(f"Virheellinen valinta.")
            nayta_valikko()

main()





