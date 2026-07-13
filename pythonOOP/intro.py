from pet import Pet

pet1 = Pet("Dog", "Scarlett", 7, True)
pet2 = Pet("Panda", "Po", 24, False)

print(pet1.name)

print(f"Hello, this is {pet2.name} speaking")

pet1.descibe()

pet1.update_age(18)
pet1.descibe