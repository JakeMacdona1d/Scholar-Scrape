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
    try:
        path = os.path.join(str(name))
        os.mkdir(path)
    except: pass
    return path

def getAbstract (url,dir):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    lines = soup.find_all('p')

    bodyContent = ""
    charCount = 0

    for line in lines:
        if len(str(line.text)) > charCount : 
            bodyContent = line.text
            charCount = len(line.text)

    text_file = open(dir+"/abstract.txt", "w")
    n = text_file.write(bodyContent)
    text_file.close()

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
            
    endofUrl = text[closest+6:].find('"')
    return text[closest+6:endofUrl + closest+6]
    
    
def querySearch (query) :
    #another user option
    # Mozilla/5.0 (Macintosh; Intel Mac OS X 0_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9
    headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari/605.1.15 Version/13.0.4'}
    #Tried using my zero-tier proxies
    # proxies = {"http": "http://172.29.15.137:9993","https": "https://172.29.15.137:16"}

    titl = query
    query = query.replace(' ','+')
    query+= '&btnG'
    url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + query
    response=requests.get(url,headers=headers)

    soup=BeautifulSoup(response.content,'lxml')

    contents = str(soup.select('[data-lid]'))

    return getLink(contents.find(titl),contents)

def saveText (fileName,dir,content) :
    text_file = open(dir + '/' + fileName, "w")
    n = text_file.write(content)
    text_file.close()


# def download_pdf(url, file_name, dir, headers):

#     # Send GET request
#     response = requests.get(url, headers=headers)

#     # Save the PDF
#     if response.status_code == 200:
#         with open(dir + '/' +file_name, "wb") as f:
#             f.write(response.content)
#     else: pass
#         # print(response.status_code)


# def savePdf(url,dir):
#     # Define HTTP Headers
#     headers = {
#         "User-Agent": "Chrome/51.0.2704.103",
#     }

#     # Define image file name
#     file_name = "file1.pdf"

#     # Download image
#     download_pdf(url, file_name, dir, headers)