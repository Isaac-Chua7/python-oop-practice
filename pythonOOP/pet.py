class Pet:
    def __init__(self, species, name, age, plays_fetch):
        self.species = species
        self.name = name
        self.age = age
        self.plays_fetch = plays_fetch
    
    def descibe(self):
        print(f"Hello my name is {self.name}, I am a {self.age} year old {self.species}")

    def update_age(self, new_age):
        self.age = new_age