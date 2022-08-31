import requests
from bs4 import BeautifulSoup


def getAbstract (url):
    # Making a GET request
    r = requests.get(url)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    lines = soup.find_all('p')

    bodyContent = ""
    charCount = 0

    for line in lines:
        if len(str(line.text)) > charCount : 
            bodyContent = line.text
            charCount = len(line.text)

    print (bodyContent)
    text_file = open("abstract.txt", "w")
    n = text_file.write(bodyContent)
    text_file.close()
getAbstract("https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:4JMBOYKVnBMC")