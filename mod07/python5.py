def kokonaisluku(lista):
    lista2 = []
    for i in lista:
        if i % 2 == 0:
            lista2.append(i)
    return lista2
         

def main():
    lista1 = [1, 2, 3,4]
    lista2 = kokonaisluku(lista1)

    print(f"{lista2}")

main()

        