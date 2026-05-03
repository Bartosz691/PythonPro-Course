from pathlib import Path

log_path = Path("log2.txt")

try:
    f = open(log_path, "a", encoding="utf-8")
    f.write("Przykładowy wpis\n")

except Exception as e:
    print("Błąd:", e)

finally:
    f.close() 