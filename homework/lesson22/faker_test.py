from faker import Faker


fake = Faker("pl_PL")


print("10 losowych polskich imion i nazwisk:")

for _ in range(10):
    print(fake.name())


print("\n10 losowych zdań:")

for _ in range(10):
    print(fake.sentence())