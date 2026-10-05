# Esineiden keräys peli #
Pelin tarkoitus on kiertää huoneita kahdessa talossa ja kerätä esineitä satunnaisesti. Peli loppuu, kun pelaaja on kerännyt kaikki esineet maailmasta.

## main.py ##
main.py tiedosto on tiedosto, josta itse peli käynnistetään. main.py tiedostoo on importattu esine.py, huone.py, pelaaja.py sekä pythonin kirjastoja (random, json ja os).

## pelaaja.py ##
pelaaja.py tiedostossa luotiin pelaaja hahmo, jolla on nimi, sijainti, ja inventory (pelissä kutsutaan repuksi.)

## huone.py ##
huone.py tiedostossa luotiin maailma funktio. Kaksi taloa (sanakirjaa), jossa on huoneita (listoja) eri esineitä varten. 

## esine.py ## 
esine.py tiedostoon ei tarvinnut laittaa mitään muuta kuin luokka esineelle.