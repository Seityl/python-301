# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`
from enum import Enum
import random

class PrimaryType(Enum):
    WATER = "Water"
    FIRE = "Fire"
    GRASS = "Grass"

class Pokemon:
    # Initialize pokemone class with pokemon name, primary type, max hp & hp
    def __init__(self, name,  primaryType, maxHp, hp):
        print(f"Initializing Pokemon w/ Name: {name}, Primary Type: {primaryType}, Max HP: {maxHp}, HP: {hp}")
        
        self.name = name
        if isinstance(primaryType, PrimaryType):
            self.primaryType = primaryType
        else:
            raise ValueError("Wrong Primary Type Provided. 'Water', 'Fire', 'Grass' Only.  ")

        self.maxHp = maxHp
        self.hp = hp

    @classmethod 
    def createRandom(cls, name, maxHp, hp):
        randomType = random.choice(list(PrimaryType))
        return cls(name, randomType, maxHp, hp)

    def __repr__(self):
        return f"Name: {self.name}, Primary Type: {self.primaryType.value}, Max HP: {self.maxHp}, HP: {self.hp}"

try:
    p1 = Pokemon("Jeriel", PrimaryType.WATER, 1000, 1000)
    print(f"Pokemon Instance Created Successfully: {p1}")
except ValueError as e:
    print("Error Occured During Creating Pokemon: ", e)

randomPokemon = Pokemon.createRandom("Random Pokemon", 1200, 1200)
print(randomPokemon)
def battle():
    pass