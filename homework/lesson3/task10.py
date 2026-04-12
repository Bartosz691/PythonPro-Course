dane_uzyt = input("Podaj swoje imię i nazwisko: ")

clean_text = dane_uzyt.strip().title()


print(f"{clean_text} długość znaków w tekście: {len(clean_text)}")
