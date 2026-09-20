import random
 
 
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
 
    def kiihdytä(self, kmh):
        self.nopeus = self.nopeus + kmh
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
 
    def kulje(self, tunti):
        self.matka = self.matka + self.nopeus * tunti
 
 
class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot
 
    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)
 
    def tulosta_tilanne(self):
        print(f"\n{self.nimi} - tilanne:")
        print(f"{'Rekisteritunnus':<16}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        print("-" * 51)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.matka:<10.0f}")
 
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus_km:
                return True
        return False
 
 
# Pääohjelma
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))
 
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
 
tunteja = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja += 1
    if tunteja % 10 == 0:
        kilpailu.tulosta_tilanne()
 
print("\nKilpailu on ohi!")
kilpailu.tulosta_tilanne()