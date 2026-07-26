while True:
    try:
        fnum = float(input("Podaj pierwszą liczbę: "))
        snum = float(input("Podaj drugą liczbę: "))
        dzialanie = input("Podaj działanie (+, -, *, /): ")

        if dzialanie == "+":
            wynik = fnum + snum
        elif dzialanie == "-":
            wynik = fnum - snum
        elif dzialanie == "*":
            wynik = fnum * snum
        elif dzialanie == "/":
            wynik = fnum / snum
        else:
            print("Niepoprawna operacja.")
            continue

    except ValueError:
        print("Błąd: musisz podać liczby.")

    except ZeroDivisionError:
        print("Błąd: nie można dzielić przez zero.")

    else:
        print(f"Wynik: {wynik}")

    finally:
        print("Kolejna operacja...")