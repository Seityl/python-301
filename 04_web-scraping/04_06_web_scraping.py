# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

def fetchContent(url):
    response = requests.get(url)
    response.raise_for_status()
    print("Success: Fetched Content")
    return response.content

def extractText(soup):
    paragraphs = soup.find_all('p')
    textContent = '\n'.join([para.get_text() for para in paragraphs])
    print("Success: Extracted Text")
    return textContent
# Fetch Page Content
url = "https://www.techtarget.com/searchsecurity/definition/SOAR"
pageContent = fetchContent(url)
# Parse Page Content
soup = BeautifulSoup(pageContent, 'html.parser')
# Extract text form page
pageText = extractText(soup)
# Print page information
print(pageText)