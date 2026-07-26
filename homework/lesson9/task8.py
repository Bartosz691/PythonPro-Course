from pathlib import Path

logs_path = Path("log.txt")
keyword = input("Podaj słowo klucz do wyszukania w logach: ")


def write_keylog(
    line: str,
    keylog_filepath: str | Path = "wyniki_wyszukiwania.txt"
):
    if not line.endswith("\n"):
        line += "\n"

    with open(keylog_filepath, "a", encoding="utf-8") as klfp:
        klfp.write(line)


# Czyścimy plik wynikowy przed rozpoczęciem nowego wyszukiwania
with open("wyniki_wyszukiwania.txt", "w", encoding="utf-8"):
    pass


with open(logs_path, "r", encoding="utf-8") as lfp:
    for line in lfp:
        if keyword in line:
            write_keylog(line)