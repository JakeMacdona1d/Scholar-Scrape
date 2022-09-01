import requests
from bs4 import BeautifulSoup


def getAbstract (url):
    # Making a GET request
    r = requests.get(url)
    print (r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    results = str(soup)

    print (results)

    desription = str("")

    subs = ["OBJECTIVE","BACKGROUND","METHODS"]
    for i in range (3):
        startTarget = '"gsh_csp"'

        if results.find('"gsp_csp') == -1: 
            startTarget = '"gsh_small"'
        endTarget = '</div>'
        results = results[int(results.find(startTarget)) + len (startTarget) + 1:]
        end = results[len(startTarget):].find(endTarget) + len (startTarget)
        desription += subs[i] + ": " + results[:end]
      
    return desription

getAbstract("https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:4JMBOYKVnBMC")