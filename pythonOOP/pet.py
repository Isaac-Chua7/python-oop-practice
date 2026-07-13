class Pet:

    num_pets = 0
    is_Animal = True

    def __init__(self, species, name, age, plays_fetch):
        self.species = species
        self.name = name
        self.age = age
        self.plays_fetch = plays_fetch
        Pet.num_pets += 1
    
    def descibe(self):
        print(f"Hello my name is {self.name}, I am a {self.age} year old {self.species}")

    def update_age(self, new_age):
        self.age = new_age
