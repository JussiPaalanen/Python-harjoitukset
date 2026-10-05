from pelaaja import Pelaaja
from huone import Huone, maailma
from esine import Esine
import random
import json

#Ohjelma aluksi printtaa käyttyäjälle pelin intron ja ohjeet

def lue_tiedosto(tiedostonimi):
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Tiedostoa {tiedostonimi} ei löytynyt.")

#Tehdään tallennus komennot peliä varten. Missä vaan tilanteessa, kun pelaaja menee päävalikkoon hän pystyy
#tallentamaan pelin ja ladata kun aloittaa pelaamisen. 

def tallenna(pelaaja, talot):
    data = {
        "nimi": pelaaja.nimi,
        "talo": pelaaja.talo,
        "sijainti": pelaaja.sijainti.numero,
        "inventory": pelaaja.inventory,
        "talot": {},
    }
    for talon_nimi, huoneet in talot.items():
        data["talot"][talon_nimi] = {}
        for numero, huone in huoneet.items():
            data["talot"][talon_nimi][numero] = huone.esine

    with open("tallennus.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Peli tallennettu.")


def lataa(pelaaja, talot):
    try:
        with open("tallennus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Tallennusta ei löytynyt.")
        return

    for talon_nimi, huoneet in data["talot"].items():
        for numero, esineet in huoneet.items():
            talot[talon_nimi][int(numero)].esine = esineet

    pelaaja.nimi = data["nimi"]
    pelaaja.inventory = data["inventory"]
    pelaaja.talo = data["talo"]
    pelaaja.sijainti = talot[pelaaja.talo][data["sijainti"]]
    print(f"Peli ladattu. Tervetuloa takaisin, {pelaaja.nimi}!")

#Kysyy pelaajan identiteetin (Nimen ja iän), jos pelaaja on alle 12 vuotias ohjelma sanoo (olet alaikäinen)
# Ja sammuttaa pelin

def identiteetti():
        nimi = input("Mikä on pelinimesi:\n")
        ikä = int(input("Mikä on ikäsi:\n"))
        if ikä > 12:
            print(f"Tervetuloa")
            return nimi
        else:
            print(f"Olet Alaikäinen")
            exit()

#Käy läpi kaikki huoneet, jos huoneet ovat tyhjiä (eli ei ole jäljellä esineitä.)
# Palauttaa True ja main funktiossa peli onnittelee pelin läpi pelaamisesta

def kaikki_keratty(talot):
    for huoneet in talot.values():
        for huone in huoneet.values():
            if huone.esine:
                return False
    return True

#Näyttää päävälikon

def nayta_valikko():
    print("\n--- PÄÄVALIKKO ---")
    print("1. Aloita peli")
    print("2. Tallenna peli")
    print("3. Lataa peli")
    print("4. Näytä reppu")
    print("0. Lopeta")




#main funktio on itse pelin touteutus funktio


def main():
    lue_tiedosto("intro.txt")
    lue_tiedosto("ohjeet.txt")
    talot = maailma()
    nimi = identiteetti()
    pelaaja = Pelaaja(nimi, "talo1", talot["talo1"][0])
    while True:
            nayta_valikko()
            valinta = input("Valitse: ").strip()
            if valinta == "1":
                print("Ladataan peliä...")
                while True:
                    huone = pelaaja.sijainti
                    talo = pelaaja.talo
                    print(f"\nOlet talossa {pelaaja.talo}")
                    print(f"Olet huoneessa {huone.numero}")
                    print(f"Huoneessa on: {huone.esine}")
                    
                    if huone.esine:   # onko huoneessa esineitä
                        keraus = input("Haluatko kerätä esineen? (kyllä/ei): ").strip().lower()
                        if keraus == "kyllä":
                            x = random.choice(huone.esine)
                            huone.esine.remove(x)
                            pelaaja.inventory.append(x)
                            print(f"Löysit: {x}")
                            print(f"Reppu: {pelaaja.inventory}")

                            #Jos kaikki esineet kerätty, ohjelma onnittelee pelin läpäisemisestä ja peli loppuu.
                            if kaikki_keratty(talot):
                                print(f"\nOnneksi olkoon, olet kerännyt kaikki esineet.")
                                print(f"Peli loppui. Esineet: {len(pelaaja.inventory)}\n{pelaaja.inventory}")
                                return

                    komento = input("Enter = liiku, v = vaihda taloa, q = valikkoon: ").strip()
                    if komento == "q":
                        break
                    elif komento == "v":
                        uusi = "talo2" if pelaaja.talo == "talo1" else "talo1"
                        pelaaja.vaihda_taloa(talot, uusi)
                        continue
                    pelaaja.liiku(talot)

            elif valinta == "2":
                tallenna(pelaaja, talot)
            elif valinta == "3":
                lataa(pelaaja, talot)
            elif valinta == "4":
                print(pelaaja.inventory)
            elif valinta == "0":
                print(f"Lopetetaan.")
                break
            else:
                print(f"Virheellinen valinta.")

main()