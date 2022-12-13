#In progress.
# Will posibly be employed to get jpg images for website

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


def similarRGB (key, input, percentAccept) :
    maxrgb = 255
    for i in range(len(key)) :
            if percentAccept < (abs((key[i]/maxrgb) - (input[i]/maxrgb))) :
                return False
    return True

def homogenusArea (key, matrix, tolerance,checkSpace, posx, posy, width, height) :
    avg = 0
    stopped = False

    count = 1
    direction = 1

    while checkSpace > count :
        for i in range(count) :
            if posx > width or posx < 0 : return False
            if posy > height or posy < 0 : return False

            try : 
                posy += direction
                if not similarRGB(key, list(matrix[posx ,posy]), tolerance) :
                    avg += 1
            except: avg += 1

            try : 
                posx += direction
                if not similarRGB(key, list(matrix[posx ,posy]), tolerance) :
                    avg += 1
            except: avg += 1

            direction *= -1
            count += 1

            if avg / ((checkSpace)) > tolerance: 
                        stopped = True
                        break
        if not stopped : 
            return True
    return False

def getAxes(key, tolerance, domain, width, height) : 
    matrix = img.imread("output.jpg")

    x1 = y = xf = yf = -1
    #gets a pixel in color tolerance of key
    #then sees if surounding area is tolerable 
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            if similarRGB(key, list(matrix[i,j]), tolerance):
                if not x1 == -1 and not xf == -1 : return (x1, y, xf, yf)

                checkSpace = int((height * width) * domain)
                if x1 == -1 :
                    if homogenusArea(key,matrix,tolerance,checkSpace,i,j,width, height) :
                        x1 = j
                        y = i 
                if xf == -1 :
                    if homogenusArea(key,matrix,tolerance,checkSpace,width - i, height -j, width, height) :
                        xf = width - i
                        yf = height - j
                              
    return (0,0,0,0)

#Gets a screenshot of the browser with the document.
#Does not produce image of just the article.
# Assumes edge theme has been set correctly to bubblegum
def screenShot(directory, name) :
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    im=ImageGrab.grab(bbox=(0,0,width,height))
    im.save("output.jpg")

    #The theme of edge has been set to the unique color of bubblegum hex #fd70a1
    # rgb (253,112,161) 
    key = [253,112,161]


    tolerance = .05
    domain = .01
    x = y = xf = yf = 0

    (x,y,xf,yf) = getAxes(key,tolerance,domain, width, height)
    print (x,y,xf,yf)

    im=ImageGrab.grab(bbox=(x,y,xf,height))
    im.save("output.jpg")



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

# thing(20)