# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests

def get_all_characters():
    response = requests.get('https://ghibliapi.vercel.app/species')
    characters = response.json()
    return characters

def find_ghosts():
    characters = get_all_characters()
    ghosts = []
    for character in characters:
        if 'ghost' in character['name'].lower() or 'cat' in character['species'].lower():
            ghosts.append(character)
    return ghosts

ghosts = find_ghosts()
for ghost in ghosts:
    print(ghost['name'])
