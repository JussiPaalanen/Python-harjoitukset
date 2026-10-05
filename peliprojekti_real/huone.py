

class Huone:
    def __init__(self, numero, esine):
        self.numero = numero
        self.esine = esine

#Luo maailman jossa on 2 taloa, jossa on huoneita.
#Huoneilla on eri esineitä, jota pelin aikana voi kerätä
#        

def maailma():
    talot = {
        "talo1": {
            0: Huone(0, []),
            1: Huone(1, ["Haarukka", "Veitsi", "Lautanen"]),
            2: Huone(2, ["Tietokone", "Hiiri", "Näppäimistö"]),
            3: Huone(3, ["sänky", "Peitto", "Tyyny"]),
        },
        "talo2": {
            0: Huone(0, []),
            1: Huone(1, ["Kirja", "Lamppu"]),
            2: Huone(2, ["Vasara", "Naula"]),
            3: Huone(3, ["Pyörä", "Jalkapallo", "Pumppu"]),
            4: Huone(4, ["Kivääri", "Pistooli"]), 
        },
    }
    return talot