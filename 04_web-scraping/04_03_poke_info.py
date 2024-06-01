# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

BASE_URL = "https://pokeapi.co/api/v2/"

# Make API calls to fetch information about each pokemon
# Extract the necessary information from the API responses
# Write the information to an HTML
# Use HTML and CSS to style the page

import requests
from jinja2 import Template

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

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Pokémon Team</title>
    <style>
        .pokemon {
            display: inline-block;
            margin: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
        }
        .pokemon img {
            max-width: 100px;
        }
    </style>
</head>
<body>
    <h1>My Pokémon Team</h1>
    {% for pokemon in pokemonTeam %}
    <div class="pokemon">
        <h2>{{ pokemon.name }}</h2>
        <p>Number: {{ pokemon.number }}</p>
        <p>Types: {{ pokemon.types|join(', ') }}</p>
        <img src="{{ pokemon.spriteUrl }}" alt="{{ pokemon.name }}">
    </div>
    {% endfor %}
</body>
</html>
'''

# Render HTML using Jinja2 template
template = Template(html_template)
renderedHtml = template.render(pokemonTeam=pokemonTeam)

# Write HTML to a file
with open("pokemon-team.html", "w") as f:
    f.write(renderedHtml)

print("HTML file generated: pokemon-team.html")