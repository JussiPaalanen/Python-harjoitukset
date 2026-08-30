s1 = input("Kerro sukupuolesi: ")
h1 = int(input("Kerro hemoglobiiniarvo: "))

if s1 == "Mies" and h1 > 195 or s1 == "Nainen" and h1 > 175: 
    print("Hemoglobiiniarvosi ovat korkeat.")
elif s1 == "Mies" and h1 < 134 or s1 == "Nainen" and h1 < 117:
    print("Hemoglobiiniarvosi ovat matalat.")
else:
    print("Hemoglobiiniarvosi ovat normaalit.")
