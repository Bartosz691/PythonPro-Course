owoce = ["jabłko", "banan", "wiśnia"]

owoce.append("pomarańcze")


print(f"dodanie pomarańczy na końcu listy: {owoce}")
      
owoce[owoce.index("banan")] = "jagoda"

print(owoce)