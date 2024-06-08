# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.

import requests
from bs4 import BeautifulSoup

# Take name of ingredients as input and return list of ingredients from user
def getInput():
    print("- " * 9, "\nINGREDIENT SEARCH\nBY JERIEL FRANCIS\n", "- " * 9)
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
    # Create list of links found
    print("Success: Found links")
    links = []
    for link in text:
        links.append(url + link.get('href'))
    print("Success: Created list of links")
    return links

# Parse and return recipies
def getRecipies(links):
    # Recipie # counter
    n = 0
    # Dict that stores details of all recipies
    recipies = []
    for link in links:
        # List of recipie details: Title, Author, Information
        recipie = []
        response = requests.get(link)
        # Chcek if request is successful
        response.raise_for_status()
        print(f"Success: Fetched content from {link}")
        # Set page content to variable soup
        soup = response.content
        # Parse HTML content
        parsedContent = BeautifulSoup(soup, 'lxml')
        # Get recipie title & append it to the recipie details list
        recipieTitle = parsedContent.body.find('h1', attrs={'class':'title is-2'}).text
        recipie.append(recipieTitle)
        # Get recipie author & append it to the recipie details list
        recipieAuthor = parsedContent.body.find('p', attrs={'class':'subtitle is-3 author'}).text
        recipie.append(recipieAuthor)
        # Get recipie information & append it to the recipie details list
        recipieInformation = parsedContent.body.find('div', attrs={'class':'md'}).text
        recipie.append(recipieInformation)
        # Add recipie details to recipies list
        recipies.append(recipie)
        print(f"Success: Added Recipie {n}")
        n += 1
    return recipies

# Search through the recepies to find one that includes the provided ingredients
def searchIngredients(recipieList, ingredientList):
    # Iterate over every recipie in the recipie list
    foundIngredients = False
    for recipie in recipieList:
        # Iterate over every detail in each recipie: Title, Author, Information
        for detail in recipie:
            # Iterate over each ingredient in the provided ingredients
            # And check if it can be found in the Title, Author or Information
            for ingredient in ingredientList:
                if ingredient in detail:
                    print("\n")
                    print("-" * 125)
                    for r in recipie:
                        print(f"\n{r}")
                    foundIngredients = True
                    break
        if foundIngredients:
            continue
    if not foundIngredients:
        ingredients = ' '.join(ingredientList)
        print(f"No recipies with {ingredients} were found.")
# Get ingredients from user
ingredientList = getInput()
# Get recipies from API
recipieList = getRecipies(fetchRecipieLinks())
# Search for the ingredients that the user inputed in the recipie list
# Print the recipies that they are found in
searchIngredients(recipieList, ingredientList)

