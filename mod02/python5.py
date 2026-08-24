leiviskät = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit "))

luoti = leiviskät * 20 * 32 + naulat * 32 + luodit
yht_grammat = luoti * 13.3
kilogrammat = int(yht_grammat // 1000)
grammat = yht_grammat % 1000

print(f"Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")



