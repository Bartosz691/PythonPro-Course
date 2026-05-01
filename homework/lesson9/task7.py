from pathlib import Path

# Tworzenie ścieżki
sciezka_do_pliku = Path("Projekt") /"src" /"data" /"docs"
# Tworzenie folderów, jeśli nie istnieją
sciezka_do_pliku.parent.mkdir(parents=True, exist_ok=True)

# Zapis do pliku
with open(sciezka_do_pliku, "w") as f:
  f.write("To jest raport.")
  
print(f"Plik istnieje: {sciezka_do_pliku.exists()}")
