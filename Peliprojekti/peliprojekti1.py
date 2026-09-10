nimi = input("Mikä on pelinimesi:\n")
ikä = int(input("Mikä on ikäsi:\n"))

print(f"{nimi}")
print(f"{ikä}")

if ikä > 12:
    print(f"Tervetuloa")

else:
    print(f"Olet Alaikäinen")
    exit()

def nayta_valikko():
    print("\n--- PÄÄVALIKKO ---")
    print("1. Peli1")
    print("2. Peli2")
    print("3. Peli3")
    print("0. Lopeta")

lista1 = [] #Pelin 1. lista

def peli1():
    while True:
        esine = input("Anna jokin esine (Enter lopettaa.): ")
        if esine != "":
            lista1.append(esine)
        else:
            break


def peli2():
    
    print(f"Tässä on lista pelistä 1. {lista1}")

lista3 = [] #Pelin kolme lista

def peli3():
    while True: 
        luku = int(input("Anna ensimmäinen luku: "))
        lista3.append(luku)
        luku2 = int(input("Anna toinen luku: "))
        lista3.append(luku2)
        luku3 = int(input("Anna viimeinen luku: "))
        lista3.append(luku3)
        summa = sum(lista3)
        print(f"Tässä on summa luvuista, jotka juuri annoit: {summa}")
        break





def main():
    while True: 
        nayta_valikko()
        valinta = input("Valitse: ").strip()

        if valinta == "1":
            print(f"Ladataan peli1...")
            peli1()
            
        elif valinta == "2":
            print(f"Ladataan peli2...")
            peli2()
            
        elif valinta == "3":
            print(f"Ladataan peli3...")
            peli3()
        elif valinta == "0":
            print(f"Lopetetaan.")
            break
        else:
            print(f"Virheellinen valinta.")
            nayta_valikko()

main()





