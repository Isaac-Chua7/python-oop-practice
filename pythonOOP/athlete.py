from extra_classes import Human, Offensive_Specialist, Defensive_Specialist

class Athlete(Human):
    def __init__(self, name, sport, height):
        self.name = name
        self.sport = sport
        self.height = height

    def introduce(self):
        print(f"Hi my name is {self.name}, I play {self.sport} and stand at {self.height} cm")
    
class Basketballer(Athlete, Defensive_Specialist):
    def score(self):
        print(f"{self.name} steps back and launches from 3")

class Volleyballer(Athlete, Offensive_Specialist):
    def score(self):
        print(f"{self.name} rises and spikes the ball down")

class Soccerer(Athlete, Offensive_Specialist):
    def score(self):
        print(f"{self.name} bends it like Beckham around the keeper")


    