zdanie = input("Podaj zdanie: ")
samogloski = "aeiouy"
samogloski += samogloski.upper()

for litera in zdanie:
    if litera not in samogloski:
        continue
    print(litera)
    