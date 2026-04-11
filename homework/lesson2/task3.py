#obliczanie obwodu prostokąta

dlugosc = float(input("Podaj długość: "))
szerokosc = float(input("Podaj szerokość: "))


def oblicz_obwod(dlugosc, szerokosc):
    obwod = 2 * (dlugosc + szerokosc)

    return obwod


if dlugosc <= 0 or szerokosc <= 0:
        print("Podano błędne wymiary!")
else: 
        obwod1 = oblicz_obwod(dlugosc, szerokosc)
        print(f"Obwód prostokąta wynosi: {obwod1}")