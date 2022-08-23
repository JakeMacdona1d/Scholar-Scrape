import requests
from bs4 import BeautifulSoup
 
 
def getPdfUrl (url):
    # Making a GET request
    r = requests.get(url)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # find all the anchor tags with "href"
    for link in soup.find_all('a'):
        # print (link.text)
        if 'pdf' in str(link.get('href')):
            if not ('epdf' in str(link.get('href'))):
                print(link.get('href'))
    