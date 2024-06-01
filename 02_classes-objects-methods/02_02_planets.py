# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, name, mass, circumference, type, location):
        self.name = name
        self.mass = mass
        self.circumference = circumference
        self.type = type
        self.location = location
    def __repr__(self) -> str:
        return f"Planet(name={self.name},mass={self.mass}, circumference={self.circumference}, type={self.type}, location={self.location})"

earth = Planet("earth", "4000,000,000 kg", "40,000 km", "terrestrial", "the solar system")
print(earth)