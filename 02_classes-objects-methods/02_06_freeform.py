# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Animal:
    """Defines an animal."""
    def __init__(self, type, breed, color):
        self.type = type
        self.breed = breed
        self.color = color
        
    def __add__(self, other):
        newType = self.type + other.type
        newColor = self.color + other.color
        newBreed = self.breed + other.breed
        return Animal(type=newType, color=newColor, breed=newBreed)
        
    def __str__(self) -> str:
        return f"Animal(type={self.type}, breed={self.breed}, color={self.color})"
        
class Person:
    """Defines a person."""
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def __add__(self, other):
        newName = self.name + other.name
        newAge = self.age + other.age
        newHobby = self.hobby + other.hobby
        return Person(name=newName, age=newAge, breed=newHobby)
        
    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age}, hobby={self.hobby})"
        
class Phone:
    """Defines a new phone."""
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def __add__(self, other):
        newBrand = self.brand + other.brand
        newmodel = self.model + other.model
        newStorage = self.storage + other.storage
        return Person(brand=newBrand, model=newmodel, breed=newStorage)
        
    def __str__(self) -> str:
        return f"Person(brand={self.brand}, model={self.model}, storage={self.storage})"
    
a1 = Animal("Dog", "German Shepard", "Black")
a2 = Animal("Cat", "Regular", "White")
p1 = Person("Jeriel", 18, "Gym")
p2 = Person("Yaushy", 21, "Cooking")
c1 = Phone("Samsung", "Galaxy S24 Ultra", "512GB")
c2 = Phone("Apple", "iPhone 15 Pro Max", "512GB")

print(f"{a1}\n{a2}\n{p1}\n{p2}\n{c1}\n{c2}")