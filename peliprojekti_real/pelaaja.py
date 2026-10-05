import random

#luodaan pelaaja

class Pelaaja:
    def __init__(self, nimi, talo, sijainti):
        self.nimi = nimi
        self.talo = talo
        self.sijainti = sijainti 
        self.inventory = []

#Pelaajan liikuminen
    
    def liiku(self, talot):
        huoneet = talot[self.talo]
        numero = random.randint(0, len(huoneet) - 1)
        self.sijainti = huoneet[numero]
        print(f"Siirryit huoneeseen {numero}.")

#Talon vaihtaminen

    def vaihda_taloa(self, talot, uusi_talo):
        self.talo = uusi_talo
        self.sijainti = talot[uusi_talo][0]   # aloitetaan huoneesta 0
        print(f"Siirryit taloon {uusi_talo}.")
