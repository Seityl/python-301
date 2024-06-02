# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.


import requests

def fetchCats():
    # Get all the cats n em
    url = "https://ghibliapi.vercel.app/people"
    response = requests.get(url)
    if response.status_code == 200:
        print("Successfully fetched cats")
        characters = response.json()
        cats = [character for character in characters if character['species'].endswith('/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3')]
        return cats
    else:
        print(f"Failed. Error Code: {response.status_code}")

# Pokemon List
pokemon = ["pikachu", "charizard", "squirtle", "diglett", "mewtwo", "rattata"]

# Fetch Pokemon data from PokeAPI
def fetchPokemonData(pokemonName):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemonData = {
            "name": data["name"].capitalize(),
            "number": data["id"],
            "types": [t["type"]["name"].capitalize() for t in data["types"]],
            "spriteUrl": data["sprites"]["front_default"]
        }
        print(f"Successfully retrieved data for {pokemonName}")
        return pokemonData
    else:
        print(f"Failed to retrieve data for {pokemonName}")
        return None
    
# Fetch data for each pokemon
pokemonTeam = [fetchPokemonData(name) for name in pokemon]
# Fetch data for each cat
cats = fetchCats()
print(pokemonTeam[0]['name'] + " " + cats[0]['name'])