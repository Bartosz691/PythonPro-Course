from pathlib import Path


file_path = Path("plik.txt")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        zawartosc = f.read()
        print(zawartosc)

except FileNotFoundError:
    print("Plik nie istnieje.")

except PermissionError:
    print("Brak uprawnień do odczytu pliku.")