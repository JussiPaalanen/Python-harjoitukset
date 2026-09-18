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

   
a1 = Auto("ABC-123", 142)

a1.kiihdytä(60)

a1.kulje(1.5)


print(f"Auton nopeus = {a1.nopeus}km/h\nMatka ajettu: {a1.matka}")

#a1.kiihdytä(-200)

#print(f"Äkki jarrutuksen jälkeen nopeus on = {a1.nopeus}km/h")