# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.vercel.app/ in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests

url = "https://ghibliapi.vercel.app/people"

response = requests.get(url)

if response.status_code == 200:

    print("Success")
    
    characters = response.json()

    cats = [character for character in characters if character['species'].endswith('/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3')]

    print("-" * 100)

    for cat in cats:
        print(f"Name: {cat['name']}")
        print(f"Gender: {cat['gender']}")
        print(f"Age: {cat['age']}")
        print(f"Eye Color: {cat['eye_color']}")
        print(f"Hair Color: {cat['hair_color']}")
        print(f"Films: {cat['films']}")
        print("-" * 100)
else:
    print(f"Failed. Error Code: {response.status_code}")


