import requests
import pyscreenshot as ImageGrab
import tkinter
import os
import time
import webbrowser
from bs4 import BeautifulSoup
import matplotlib.image as img
import numpy as np


def openWebPage (url) :
    #Using edge browers b/c I do not use it
    edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    webbrowser.get('edge').open(url)



def screenShot(directory, name) :
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    #getting half width b/c webPage opens as half screen on right side
    im=ImageGrab.grab(bbox=(0,0,width,height))
    im.save("output.jpg")

    #The theme of edge has been set to the unique color of salmon hex #fd70a1
    # rgb (253,112,161) 

    matrix = img.imread("output.jpg")

    for i in matrix :
        for j in i :
            if j == ([50,50,50]) :
                print (j)

    # print (matrix)





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
                return link.get('href')



def getArticleJpeg () :
    # Define HTTP Headers
    headers = {
        "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    # Define image file name
    fileName = "file1.pdf"

    dir = ".../output/images"

    # Define URL of an image
    url = getPdfUrl("https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:4JMBOYKVnBMC")

    openWebPage(url)

    #waiting for page to open before screenshot
    time.sleep(10)

    screenShot(dir, fileName)

    
    # waiting for screenShot
    time.sleep(5)
    os.system("taskkill /im msedge.exe /f")

    
getArticleJpeg()
