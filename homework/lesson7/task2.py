oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}

posortowane_po_ocenie = sorted(oceny, key=lambda oceny: oceny[1])
print(posortowane_po_ocenie)
