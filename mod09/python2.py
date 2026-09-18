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
   
a1 = Auto("ABC-123", 142)

a1.kiihdytä(30)
a1.kiihdytä(70)
a1.kiihdytä(50)

print(f"Auton nopeus = {a1.nopeus}km/h")

a1.kiihdytä(-200)

print(f"Äkki jarrutuksen jälkeen nopeus on = {a1.nopeus}km/h")