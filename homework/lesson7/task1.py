slowa = ["jablko", "banan", "kiwi", "gruszka", "truskawka"]
slowa_filtered = [slowo for slowo in slowa if len(slowo) > 5]
print(slowa_filtered)

print(list(filter(lambda x: len(x) > 5, slowa)))

