class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulostatiedot(self):
        print(f"Kirja\nNimi: {j1.nimi}\nKirjoittaja: {j1.kirjoittaja}\nSivumäärä: {j1.sivumaara}")
        print("-" * 25)

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulostatiedot(self):
        print(f"Lehti\nNimi: {j2.nimi}\nPäätoimittaja: {j2.päätoimittaja}")

j1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
j2 = Lehti("Aku Ankka", "Aki Hyyppä")


j1.tulostatiedot()
j2.tulostatiedot()


