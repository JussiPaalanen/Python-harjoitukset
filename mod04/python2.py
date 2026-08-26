while True:
    tuumat = float(input("Anna tuumat (Negatiivinen lopettaa): "))

    if tuumat < 0:
        print("Ohjelma lopettaa. ")
        break

    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa = sentit {sentit:.2f} cm.")
    