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