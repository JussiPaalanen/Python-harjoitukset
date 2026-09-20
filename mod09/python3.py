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
 
 
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))
 
while not any(auto.matka >= 10000 for auto in autot):
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)
 

print(f"{'Rekisteritunnus':<16}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.matka:<10.0f}")
 