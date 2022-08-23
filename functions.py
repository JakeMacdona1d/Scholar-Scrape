import os
import requests
from bs4 import BeautifulSoup

def mkDir(name):
    if len(name) > 10:
        name = name[:10]
    name = name.replace('\\\\','/')
    name = name.replace(' ','_')
    name = name.replace('/','_')

    path = os.getcwd() + str(name)
    print (name)
    try:
        path = os.path.join(str(name))
        os.mkdir(path)
    except: pass
    return path

def getAbstract (url,dir):
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
    text_file = open(dir+"/abstract.txt", "w")
    n = text_file.write(bodyContent)
    text_file.close()


def download_pdf(url, file_name, dir, headers):

    # Send GET request
    response = requests.get(url, headers=headers)

    # Save the PDF
    if response.status_code == 200:
        with open(dir + '/' +file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


def savePdf(url,dir):
    # Define HTTP Headers
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }

    # Define image file name
    file_name = "file1.pdf"

    # Download image
    download_pdf(url, file_name, dir, headers)

def getLink (start, text) :
    closest = 0
    for i in range(len(text)) :
        index = start + (i * -1)
        if text[index] == 'h':
            href = text[index: (index) +4 ]
            if href == 'href':
                print (index)
                closest = index
                break
            
    print (text[closest+6])
    endofUrl = text[closest+6:].find('"')
    print (closest+endofUrl +6)
    print (text[closest+6:endofUrl + closest+6])
    return text[closest+6:endofUrl + closest+6]
    
    
def querySearch (query) :
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 0_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    # query = 'Designing human-autonomy teaming experiments through reinforcement learning'
    # titl = 'Designing human-autonomy teaming experiments through reinforcement learning'

    # 'Fostering Human-Agent Team Leadership by Leveraging Human Teaming Principles'
    titl = query
    query = query.replace(' ','+')
    query+= '&btnG'
    url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + query
    response=requests.get(url,headers=headers)
    print (response)
    soup=BeautifulSoup(response.content,'lxml')

    print(soup.select('[data-lid]'))

    contents = str(soup.select('[data-lid]'))

    print (contents.find(titl))

    return getLink(contents.find(titl),contents)

def saveText (fileName,dir,content) :
    text_file = open(dir + '/' + fileName, "w")
    n = text_file.write(content)
    text_file.close()
