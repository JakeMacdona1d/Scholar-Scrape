from serpapi import GoogleSearch
import json
from dynamicArr import *
import requests
from bs4 import BeautifulSoup
import time
import random
import os

def getDate (content) :
  lookItem = "Publication date"
  start = str(content).find(lookItem) + len(lookItem)
  content = content[start:]
  lookItem = 'gsc_oci_value">'
  start = str(content).find(lookItem) + len(lookItem)
  content = content[start:]
  lookItem = '<'
  end = str(content).find(lookItem)
  return content[:end]

#Reduce given abrev name to just last name. 
#Useful as search item.
def reduce (name) :
    while not name.find(' ') == -1 :
        name = name[name.find(' ')+1:]
    return name

def getFull (search, input) :
    if str(search).find(input) == -1 : return None
    endIndex = str(search).find(input) + len(input) -1

    output = ""
    i = endIndex
    while not (search[i] == ',' or i < 0 or search[i] == '>') :
        output = search[i] + output
        i -= 1
    return output.strip()

def betterAuthNames(abname, content) :
    names = abname.split(',')
    product = ""
    for i in names :
        lastN = reduce(i)
        extendedName = getFull(content, lastN)
        if extendedName == None :
            product += i + ', '
        else : product += (getFull(content, lastN)) + ', '

    product = product [:len(product)-2]
    return product

# For making single repo of article data
def addToMaster (readFileName, FILE) :
  if ".json" in readFileName :
    f = open(readFileName, "r")
    addition = str(f.read())
    addition = addition.replace('"title"','title')
    addition = addition.replace('"authors"','author')
    addition = addition.replace('"link"','link')
    addition = addition.replace('"abstract"','abstract')
    addition = addition.replace('"date"','date')

    FILE.write(addition + ",\n")

def getContent (url, auths): 
    #helps with not being blocked by scholar
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
    except : 
      print ("We have been found")
      return "found", "found", "found"

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    soup2 = BeautifulSoup(r.text, 'html.parser')
    
    searchItem = ">Authors</div><div class"
    startIndex = str(soup2).find(searchItem)
    forNames = str(soup2)[startIndex: startIndex + (len(auths.split(','))*25) + len(searchItem) * 3]
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
            break

        endTarget = '</div>'
        results = results[int(results.find(startTarget)) + len (startTarget) + 1:]
        end = results[len(startTarget):].find(endTarget) + len (startTarget)
        desription += subs[i] + ": " + results[:end]

    return (desription, str(betterAuthNames(auths,forNames)),str(getDate(str(soup2))))

# container for elements of Google Scholar articles 
class ArtItem:
    title = "'title': '"
    link = "'link': '"
    authors = "'authors': '"
    abstract = ""
    date = ""

    def setLink (self,text):
      text = text.replace('"',"'") #needed b/c inconsistent html formats
      searchStartItem = "'link': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.link = text[start:end + start]
      self.link = str(self.link).replace("'",'')
      self.link = str(self.link).replace('link: ','')

    def setTit (self,text):
      text = text.replace('"',"'")
      searchStartItem = "'title': "
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.title = text[start:end + start]
      self.title = str(self.title).replace("'",'')
      self.title = str(self.title).replace("title: ",'')

    
    def setAuth (self,text):
      text = text.replace('"',"'")
      searchStartItem = "'authors': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.authors = text[start:end + start]
      self.authors = str(self.authors).replace("'",'')
      self.authors = str(self.authors).replace("authors: ",'')

# to isolate all articles discovered in SerapAPI search
def divide(text):
  temp = text
  arr = DynamicArray ()
  searchItem = "title"

  while (1) :
    found = temp.find(searchItem)
    if found == -1: break
    arr.append("'title" + temp[0:found])
    temp = temp[found + len(searchItem):len(temp)-found + len(searchItem)]
    
  return arr
