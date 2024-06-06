# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

import requests
from bs4 import BeautifulSoup

# Take name of ingredients as input and return list of ingredients from user
def getInput(prompt):
    ingredients = input(prompt + ' (separate values with \", \"):')
    if ingredients:
        ingredients = ingredients.split(', ')
        print("Success: Got ingredients")
        return ingredients
print(getInput("Enter Ingredients"))

# Fetch content from the recipie collection
def fetchRecipieInformation():
    # Recipie API link
    url = "https://codingnomads.github.io/recipes"
    # Send get request to API
    response = requests.get(url)
    response.raise_for_status()
    print("Success: Fetched content")
    return response.content

# Parse and return recipies
def getRecipies(soup):
    page = BeautifulSoup(soup, 'html.parser')
    text = page.find_all('a')
    recipies = []
    for r in text:
        recipies.append(r.get_text())
    allRecipies = '\n'.join(recipies)
    return allRecipies

# Search through the receipts to find one that includes the provided ingredients

print(getRecipies(fetchRecipieInformation()))
