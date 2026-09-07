luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print(f"luku ei ole alkuluku")
else: 
    on_alkuluku = True

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        on_alkuluku = False
        break

    if on_alkuluku:
        print(f"{luku} on alkuluku")
    else:
        print(f"{luku} ei ole alkuluku.")