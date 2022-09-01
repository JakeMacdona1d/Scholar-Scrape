from serpapi import GoogleSearch
import json
from dynamicArr import *

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

params = {
  "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
    "engine": "google_scholar_author",
    "author_id": "G1CnZ38AAAAJ",
    "hl": "en",
}



search = GoogleSearch(params)
results = dict(search.get_dict())
first = str(results.get('articles'))


articles = DynamicArray ()
strArr = divide(first)
for i in range(len(strArr)) :
  # print (strArr[i])
  item = ArtItem
  item.setTit(item,strArr[i])
  item.setLink(item,strArr[i])
  item.setAuth(item,strArr[i])
  articles.append(item)
  print (item.title)
  print (item.link)
  print (item.authors)

  # print (item.search(item))
