a = "LUX"
b = "A"
c = "B"
d = "C"

x = (input("Mikä on hyttiluokkasi: "))

if x == a:
    print("LUX on parvekkeellinen hytti yläkannella")
elif x == b:
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif x == c:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif x == d:
    print("C on ikkunaton hytti yläkannen alapuolella.")
else: 
    print("Virheellinen hyttiluokka.")


