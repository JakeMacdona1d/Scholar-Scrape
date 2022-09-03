from serpapi import GoogleSearch
import json
from dynamicArr import *
import requests
from bs4 import BeautifulSoup
import time
import random


def getAbstract (url):
    user_agent_list = [
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
      ]
    user_agent = random.choice(user_agent_list)
    headers = {'User_Agent':user_agent}

    r = requests.get(url,headers=headers,)
     
    try:
      if not str(r) == "<Response [200]>" : raise Exception
    except : print ("We have been found")

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

    for i in range (len(subs)):
        startTarget = '"gsh_csp"'

        if results.find(startTarget) == -1 :
          startTarget = '"gsh_small"'
          if results.find(startTarget) == -1 :
            return "no abstract"

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
