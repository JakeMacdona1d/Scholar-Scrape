import requests
from bs4 import BeautifulSoup


def getAbstract (url):
    # Making a GET request
    r = requests.get(url)
    print (r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    results = str(soup)
    # print (soup)

    # 3 b/c obj, background, and methods
    for i in range (3): 
        target = '"gsh_csp"'
        results = results[int(results.find(target)) + len (target):]
    
        end = results[len(target):].find(target)
        print (end)
        desription = results[:end]
        print (desription)

        bodyContent = ""
        charCount = 0

    # for line in lines:
    #     if len(str(line.text)) > charCount : 
    #         bodyContent = line.text
    #         charCount = len(line.text)

    # print (bodyContent)
    # text_file = open("abstract.txt", "w")
    # n = text_file.write(bodyContent)
    # text_file.close()
getAbstract("https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:4JMBOYKVnBMC")