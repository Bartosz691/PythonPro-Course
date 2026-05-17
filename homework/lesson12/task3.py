class KonwerterWalut:
    @staticmethod
    def usd_na_pln(kwota, kurs):
        kwota_pln = float(kwota/kurs)
        return kwota_pln
    
kwota = float(input("Podaj kwotę w USD: "))
kurs = 4

value = KonwerterWalut.usd_na_pln(kwota, kurs)
print(f"Wartość kwoty w USD: {kwota} po przeliczeniu na PLN wynosi: {value}")