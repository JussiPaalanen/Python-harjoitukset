import math

def yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 100) / 2   # muunnetaan senttimetrit metreiksi ja lasketaan säde
    pinta_ala = math.pi * sade_m ** 2     # ympyrän pinta-ala neliömetreinä
    return hinta / pinta_ala              # euroa per neliömetri

def main():
    print("Pizza 1:")
    halkaisija1 = float(input("Halkaisija (cm): "))
    hinta1 = float(input("Hinta (€): "))

    print("Pizza 2:")
    halkaisija2 = float(input("Halkaisija (cm): "))
    hinta2 = float(input("Hinta (€): "))

    hinta_per_m2_1 = yksikkohinta(halkaisija1, hinta1)
    hinta_per_m2_2 = yksikkohinta(halkaisija2, hinta2)

    print(f"Pizza 1 yksikköhinta: {hinta_per_m2_1:.2f} €/m²")
    print(f"Pizza 2 yksikköhinta: {hinta_per_m2_2:.2f} €/m²")

    if hinta_per_m2_1 < hinta_per_m2_2:
        print("Pizza 1 antaa paremman vastineen rahalle.")
    elif hinta_per_m2_2 < hinta_per_m2_1:
        print("Pizza 2 antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat saman vastineen rahalle.")

main()