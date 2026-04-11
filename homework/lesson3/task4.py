from datetime import date, datetime
dzis = date.today()

imie = input("Podaj swoje imię ")
str_birthday = input("Podaj date swoich urodzin: ")

birthday = datetime.strptime(str_birthday,"%d.%m.%Y").date()

wiek = dzis.year - birthday.year

print(f"{imie}, masz, {wiek}, lat")