class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

   
a1 = Auto("ABC-123", 142)


print(f"Rekisterinumero: {a1.rekisteritunnus}\nHuippunopeus: {a1.huippunopeus}\nNopeus = {a1.nopeus}\nMatka = {a1.matka}\n")