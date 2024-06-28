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

import random

class Pokemon:
    # Initialize pokemon class with pokemon name, primary type, max hp & hp
    def __init__(self, name,  primaryType, maxHp, hp):
        print(f"--Initializing Pokemon--\nName: {name}, Primary Type: {primaryType}, Max HP: {maxHp}, HP: {hp}\n")

        # Set Name
        self.name = name

        # Set Primary Type
        primaryType = primaryType.lower()
        if primaryType == 'water' or primaryType == 'fire' or primaryType == 'grass':
            self.primaryType = primaryType.capitalize()
        else:
            raise ValueError("Wrong Primary Type Provided. 'Water', 'Fire', 'Grass' Only.  ")

        # Set Max HP
        self.maxHp = maxHp
        # Set HP
        self.hp = hp

    @classmethod 
    def createRandom(cls):
        name = str(input("Enter Pokemon Name: "))
        maxHp = random.randint(1, 100)
        hp = maxHp
        types = ['Water', 'Fire', 'Grass']
        randomType = random.choice(types)
        return cls(name, randomType, maxHp, hp)

    # TODO: This should remove a random % of the pokemon's HP
    def damage(self):
        damage = random.randint(0, self.hp)
        self.hp -= damage
        return f"\n{self.name} took {damage} damage.\n"
        
    # TODO: This should restore a random % of the pokemon's HP
    def feed(self):
        heal = random.randint(0, self.maxHp - self.hp)
        self.hp += heal
        return f"\n{self.name} healed {heal} HP.\nNow at {self.hp} HP / {self.maxHp} HP\n"

    def __repr__(self):
        return f"Name: {self.name}, Primary Type: {self.primaryType}, Max HP: {self.maxHp}, HP: {self.hp}"

# Simulated rock, paper, scissors style battle
# Loser should lose a % of their HP
#TODO: This should auto simulate the battles until the HP of one of the pokemons is <= 0
#TODO: There should be a 25% chance of healing before each battle if their hp is less than max
# Should not be able to heal to more than max HP

def battle(pokemon1, pokemon2):
    global over
    if pokemon1.hp > 0 and pokemon2.hp > 0:
        print(f"{'-' * 25}\n{pokemon1.name} VS {pokemon2.name}\n{'-' * 25}")
        # p = pokemon, PT = primary type
        p1PT = pokemon1.primaryType.lower()
        p2PT = pokemon2.primaryType.lower()
        
        winner = ''
        loser = ''
        
        if p1PT == 'water' and p2PT == 'fire':
            winner = pokemon1
            loser = pokemon2
            
            return f"{winner.name} won this battle!\n{loser.damage()}"
            
        if p2PT == 'water' and p1PT == 'fire':
            winner = pokemon2
            loser = pokemon1
            
            return f"{winner.name} won this battle!\n{loser.damage()}"
            
        if p1PT == 'water' and p2PT == 'grass': 
            winner = pokemon2
            loser = pokemon1
            
            return f"{winner.name} won this battle!\n{loser.damage()}"
            
        if p1PT == 'grass' and p2PT == 'water': 
            winner = pokemon1
            loser = pokemon2
            
            return f"{winner.name} won this battle!\n{loser.damage()}"
            
        if p1PT == 'fire' and p2PT == 'grass': 
            winner = pokemon1
            loser = pokemon2
            
            return f"{winner.name} won this battle!\n{loser.damage()}"
            
        if p2PT == 'fire' and p1PT == 'grass':
            winner = pokemon2
            loser = pokemon1
            
            return f"{winner.name} won this battle!\n{loser.damage()}"
            
        if p1PT == 'water' and p2PT == 'water':
            over = 1
            return f"Draw!"
            
        if p1PT == 'fire' and p2PT == 'fire':
            over = 1
            return f"Draw!"

        if p1PT == 'grass' and p2PT == 'grass':
            over = 1
            return f"Draw!"
    else:
        over = 1
        
try:
    p1 = Pokemon.createRandom()
    print(f"--Pokemon Instance Created Successfully--\n{p1}\n")
    
    p2 = Pokemon.createRandom()
    print(f"--Pokemon Instance Created Successfully--\n{p2}\n")

except ValueError as e:
    print("Error Occured During Creating Pokemon: ", e)

while over == 0:
    print(battle(p1, p2))