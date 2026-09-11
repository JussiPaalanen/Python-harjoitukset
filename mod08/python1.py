kuukausi = ("Talvi", "Kevät", "Kesä", "Syksy")

luku = int(input("Anna kuukauden numero (1-12): "))

if luku == 12 and luku < 3:
    print(kuukausi[0])
elif luku >= 3 and luku < 6:
    print(kuukausi[1])
elif luku >= 6 and luku < 9:
    print(kuukausi[2])
elif luku >= 9 and luku < 12:
    print(kuukausi[3])