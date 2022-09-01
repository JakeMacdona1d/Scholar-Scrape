from serpapi import GoogleSearch
import json
from dynamicArr import *
import requests
from bs4 import BeautifulSoup
import time

def getAbstract (url):
    # Making a GET request
    r = requests.get(url)
    print (r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    results = str(soup)

    desription = str("")

    subs = ["OBJECTIVE","BACKGROUND","METHODS"]
    for i in range (3):
        startTarget = '"gsh_csp"'
        endTarget = '</div>'
        results = results[int(results.find(startTarget)) + len (startTarget) + 1:]
        end = results[len(startTarget):].find(endTarget) + len (startTarget)
        desription += subs[i] + ": " + results[:end]
      
    return desription

class ArtItem:
    title = "'title': '"
    link = "'link': '"
    authors = "'authors': '"
    abstract = ""

    searchP = {
    "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
    "engine": "google_scholar_author",
    "q": "",
    "hl": "en",
    }

    def setLink (self,text):
      searchStartItem = "'link': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.link = text[start:end + start]
      self.link = str(self.link).replace("'",'')
      self.link = str(self.link).replace('link: ','')
      self.searchP["q"] = str(self.link)

    def setTit (self,text):
      searchStartItem = "'title': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.title = text[start:end + start]
      self.title = str(self.title).replace("'",'')
      self.title = str(self.title).replace("title: ",'')

    
    def setAuth (self,text):
      searchStartItem = "'authors': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.authors = text[start:end + start]
      self.authors = str(self.authors).replace("'",'')
      self.authors = str(self.authors).replace("authors: ",'')

    

    def search (self) :
      return GoogleSearch(self.searchP)

def divide(text):
  temp = text
  arr = DynamicArray ()
  searchItem = "title"

  while (1) :
    found = temp.find(searchItem)
    if found == -1: break
    arr.append("'title" + temp[0:found])
    temp = temp[found + len(searchItem):len(temp)-found + len(searchItem)]
    
  print (len(arr))
  return arr
