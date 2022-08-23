from bs4 import BeautifulSoup
import requests

def getLink (start, text) :
    closest = 0
    for i in range(len(text)) :
        index = start + (i * -1)
        if text[index] == 'h':
            href = text[index: (index) +4 ]
            if href == 'href':
                closest = index
                break
    
    endofUrl = text[closest+6:].find('"')
    return text[closest+6:endofUrl + closest+6]
    

def querySearch (query) :
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 0_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    # query = 'Designing human-autonomy teaming experiments through reinforcement learning'
    titl = query

    # 'Fostering Human-Agent Team Leadership by Leveraging Human Teaming Principles'
    query = query.replace(' ','+')
    query+= '&btnG'
    url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + query
    
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')

    # print(soup.select('[data-lid]'))
   
    contents = str(soup.select('[data-lid]'))

    return getLink(contents.find(titl),contents)

print(querySearch('Designing human-autonomy teaming experiments through reinforcement learning'))