#duck typing, another weay to achieve polymorphism without inheritance.

class Seagull:
    def speak(self):
        print("SCREECH!")

class Duck:
    def speak(self):
        print("QUACK!")

birds = [Seagull(), Duck()]

for b in birds:
    b.speak()
    
