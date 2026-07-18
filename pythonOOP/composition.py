
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheel:
    def __init__(self, wheel_diameter):
        self.diameter = wheel_diameter

class Car:
    def __init__(self, make, model, horsepower, wheel_diameter):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = []
        for i in range (4):
            self.wheels.append(Wheel(wheel_diameter))

    def display(self):
        print(f"This car is a {self.make} {self.model} with {self.engine.horsepower} (hp) and a wheel size of {self.wheels[0].diameter} inches")

c1 = Car("Audi", "RS e-tron GT", 670, 20)
c1.display()

c2 = Car("Range Rover", "Evoque", 250, 18)
c2.display()