import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://dl.acm.org/doi/abs/10.1145/3406499.3415077')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# find all the anchor tags with "href"
for link in soup.find_all('a'):
    # print (link.text)
    if 'pdf' in str(link.get('href')):
        if not ('epdf' in str(link.get('href'))):
            print(link.get('href'))
    