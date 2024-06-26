# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
    def __init__(self, model, year, maxSpeed):
        self.model = model
        self.year = year
        self.maxSpeed = maxSpeed
    def increaseSpeed(self):
        self.maxSpeed += 5
    def __str__(self) -> str:
        return f"Car(model={self.model}, year={self.year}, maxspeed={self.maxSpeed})"

car1 = Car("M5", 2025, 350)
car2 = Car("Carrera GT", 2005, 400)
print(car1)
car1.increaseSpeed()
print(car1)
car1.maxSpeed = 360
print(car1)

print(car2)
car2.increaseSpeed()
print(car2)
car2.maxSpeed = 410
print(car2)