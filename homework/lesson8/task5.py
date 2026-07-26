while True:
    log = open("log.txt", "a", encoding="utf-8")

    try:
        fnum = float(input("Podaj pierwszą liczbę: "))
        snum = float(input("Podaj drugą liczbę: "))
        dzialanie = input(
            "Podaj działanie (+, -, *, /) lub 'koniec': "
        )

        if dzialanie == "koniec":
            break

        if dzialanie == "+":
            wynik = fnum + snum
        elif dzialanie == "-":
            wynik = fnum - snum
        elif dzialanie == "*":
            wynik = fnum * snum
        elif dzialanie == "/":
            wynik = fnum / snum
        else:
            raise ValueError("Niepoprawna operacja.")

    except (ValueError, ZeroDivisionError) as e:
        print("Wystąpił błąd:", e)
        log.write(f"{type(e).__name__}: {e}\n")

    else:
        print("Wynik:", wynik)

    finally:
        log.close()
        print("Kolejna operacja...")