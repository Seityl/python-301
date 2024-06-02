# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.
import requests
import re
from bs4 import BeautifulSoup

# Fetches the content of the given URL
def fetchContent(url):
    response = requests.get(url)
    response.raise_for_status()
    print("Success: Fetched Content")
    return response.content

# Extracts the links found
def extractLinks(soup):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/') and ':' not in href:
            fullUrl = 'https://wikipedia.org/' + href
            links.append(fullUrl)
    print("Success: Extracted Links")
    return links

# Extracts the text found
def extractText(soup):
    paragraphs = soup.find_all('p')
    textContent = '\n'.join([para.get_text() for para in paragraphs])
    print("Success: Extracted Text")
    return textContent

# Saves text to file
def saveToFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Use RegExp to find all numbers in the text
def findAllNumbers(pattern, text):
    numbers = re.findall(pattern, text)
    return numbers

# Fetch the Wikipedia page on web scraping
wikiUrl = "https://en.wikipedia.org/wiki/Web_scraping"
pageContent = fetchContent(wikiUrl)

# Parse the page content and extract links
soup = BeautifulSoup(pageContent, 'html.parser')
links = extractLinks(soup)

# Follow one of the links to another Wikipedia article
if links:
    followLink = links[0] #Follow first link
    linkedPageContent = fetchContent(followLink)
    linkedSoup = BeautifulSoup(linkedPageContent, 'html.parser')

    # Extract text content and save it to a local text file
    textContent = extractText(linkedSoup)
    saveToFile('wikipedia-article-text.txt', textContent)

    print(f"Text content from {followLink} has been saved to wikipedia-article-text.txt")
else:
    print("No valid links found on the wikipedia page.")

# Find all numbers in the text
print("Numbers in text:")
print(findAllNumbers(r'\d+', str(pageContent)))