class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
 
    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
 
    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
 
    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()
 
 
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_lukumäärä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))
 
    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
 
    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)
 
 
# Pääohjelma
talo = Talo(0, 10, 3)
talo.aja_hissiä(0, 7)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 10)
 
print("Palohälytys!")
talo.palohälytys()