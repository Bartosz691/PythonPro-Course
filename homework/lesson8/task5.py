from pathlib import Path

log_path = Path("log.txt")

while True:
    try:
        fnum = float(input("Podaj pierwszą liczbę: "))
        snum = float(input("Podaj drugą liczbę: "))
        dzialanie = str(input("Podaj znak działania [+,-,/,*] lub koniec, aby zakończyć "))

        if dzialanie == "koniec":
            break

        func_dict = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }

        wynik = func_dict[dzialanie](fnum, snum)
        print("Wynik:", wynik)

    except Exception as e:
        print("Wystąpił błąd:", e)


        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"Błąd: {type(e).__name__} - {e}\n")

    finally:
        print("Kolejna runda...\n")