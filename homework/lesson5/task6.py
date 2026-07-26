sekret = 42

while True:
    liczba = int(input("Podaj liczbę: "))

    if liczba == sekret:
        print("Gratulacje! Odgadłeś liczbę!")
        break
    else:
        print("Zła liczba. Spróbuj ponownie.")