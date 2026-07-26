def stworz_licznik():
    licznik = 0

    def zwieksz():
        nonlocal licznik

        licznik += 1

        return licznik

    return zwieksz


licznik = stworz_licznik()

print(licznik())
print(licznik())
print(licznik())
print(licznik())