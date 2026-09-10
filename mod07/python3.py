def gallonat_litroiksi(gallonat):
       return gallonat * 3.785


def main():
    while True:
        gallonat = float(input("Anna gallomäärä: "))
        if gallonat < 0:
                    break
        litra = gallonat_litroiksi(gallonat)
        print(f"{litra}")

main()

