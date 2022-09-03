import requests
from bs4 import BeautifulSoup
import random



def getAbstract (url):
    user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    
    print ("The URL is : ")
    print (url)

    user_agent = random.choice(user_agent_list)


    headers = {'User_Agent':user_agent}

    r = requests.get(url,headers=headers,)
    
    print (r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    results = str(soup)

    desription = str("")

    subs = ["OBJECTIVE","BACKGROUND","METHODS"]

    if results.lower().find('objective') == -1 :
        subs.remove('OBJECTIVE')
    if results.lower().find('background') == -1 :
        subs.remove('BACKGROUND')
    if results.lower().find('methods') == -1 :
        subs.remove('METHODS')

    for i in range (3):
        startTarget = '"gsh_csp"'
        endTarget = '</div>'

        results = results[int(results.find(startTarget)) + len (startTarget) + 1:]
        end = results[len(startTarget):].find(endTarget) + len (startTarget)
        desription += subs[i] + ": " + results[:end]
    
   
    print (desription)

    bodyContent = ""
    charCount = 0

link = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:5nxA0vEk-isC"
getAbstract(link)