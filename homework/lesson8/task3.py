

def wczytaj_plik():
    sciezka = input("Podaj ścieżkę do pliku: ")
    try:
        plik = open(sciezka, mode='r')
    except FileNotFoundError:
        print(f"plik o nazwie: {sciezka} nie istnieje ")
    except PermissionError:
        print(f"brak dostępu do pliku {sciezka}")
    finally:     
     plik.close()
     
wczytaj_plik()
