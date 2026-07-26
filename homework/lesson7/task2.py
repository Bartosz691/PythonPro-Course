oceny = {
    "Jan": 4,
    "Anna": 5,
    "Piotr": 3,
    "Kasia": 4
}

posortowane_oceny = sorted(
    oceny.items(),
    key=lambda element: element[1],
    reverse=True
)

print(posortowane_oceny)