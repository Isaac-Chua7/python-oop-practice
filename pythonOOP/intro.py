from pet import Pet
from athlete import Athlete, Basketballer, Volleyballer, Soccerer

pet1 = Pet("Dog", "Scarlett", 7, True)
pet2 = Pet("Panda", "Po", 24, False)

print(pet1.name)

print(f"Hello, this is {pet2.name} speaking")

pet1.descibe()

pet1.update_age(18)
pet1.descibe

print(f"there are currently {Pet.num_pets} pets")
if(Pet.is_Animal == True):
    print("Pets are animals")
else:
    print("Pets are not animals")

print()
print("*********************************************")
print()

athlete1 = Basketballer("Luka Doncic", "Basketball", 203)
athlete2 = Volleyballer("Shoyo Hinata", "Volleyball", 163)
athlete3 = Soccerer("Lionel Messi", "Soccer", 170)

athletes = [athlete1, athlete2, athlete3]

for a in athletes:
    a.introduce()
    a.score()
    print()

