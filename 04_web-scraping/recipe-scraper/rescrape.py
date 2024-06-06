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
def getInput():
    ingredients = input("Input Ingredients (separate values with \', \'): ")
    if ingredients:
        ingredients = ingredients.split(', ')
        print("Success: Got ingredients")
        return ingredients

# Fetch links from the recipie collection
def fetchRecipieLinks():
    # Recipie API link
    url = "https://codingnomads.github.io/recipes/"
    # Send get request to API
    response = requests.get(url)
    # Chcek if request is successful
    response.raise_for_status()
    print("Success: Fetched content")
    # Set page content to variable soup
    soup = response.content
    # Parse page content
    page = BeautifulSoup(soup, 'html.parser')
    # Look for all links <a>  in the page 
    text = page.find_all('a')
    links = []
    for link in text:
        links.append(url + link.get('href'))
    allLinks = '\n'.join(links)
    return allLinks

print(fetchRecipieLinks())

# Parse and return recipies
def getRecipies(soup):
    pass
# Search through the receipts to find one that includes the provided ingredients
