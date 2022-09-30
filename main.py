#Jake Macdonald 
# 9/23/2022
# Designed to produce json files with details of all articles authored by choice person.
#Retrives title, authors, url, and description

from util import *
import os.path


def main (start) :
  params = {
    "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
      "engine": "google_scholar_author",
      "author_id": "G1CnZ38AAAAJ", #Nathan's Id
      "hl": "en",
      "sort": "pubdate",
      "num": "100",
      "start": str(start),
  }

  search = GoogleSearch(params)
  results = dict(search.get_dict())
  first = str(results.get('articles'))


  strArr = divide(first)
  for i in range(len(strArr)) :
    if i == 0  : continue #b/c weirdness of DS

    item = ArtItem
    item.setTit(item,strArr[i])
    item.setLink(item,strArr[i])
    item.setAuth(item,strArr[i])

    fName = item.title
    sizeOfName = len(fName)
    if not sizeOfName :
      fName = item.authors 
      sizeOfName = len (fName)
    if sizeOfName > 15:
      fName = fName[:15]

    fName = fName.replace('"',"")
    fName = fName.replace('/',"")
    fName = fName.replace(' ',"")
    fName += str(sizeOfName)

    # Checking if file already exists
    try:
      with open('datCache/ ' + fName +'.json', 'r') as json_file:
        json_file.close()
        continue
    except IOError:
        pass
   
    
    baseTime = 10.0
    time.sleep(baseTime + (baseTime * random.random()))

    print (item.authors)

    (item.abstract, item.authors) = getAbstract(str(item.link),str(item.authors)) 
    if item.abstract == 'found' : return

    dictPort = {
      'title' : item.title, 
      'authors' : item.authors,
      'link' : item.link,
      'abstract' : item.abstract
    }


    with open('datCache/ ' + fName +'.json', 'w') as json_file:
      json.dump(dictPort, json_file)  
      json_file.close()

    return 404

#serpAPI only allows 100 articles to be retrieved per search
numArt = 130
iterate = 0
recompile = False
while numArt > 0 : 
  if not main(iterate * 100) == None:
    recompile = True 
  numArt -= 100
  iterate += 1

#used to make a single js file with all objects defined in the json files
if recompile :
  path = "datCache"
  dir_list = os.listdir(path)
  new = open("publications.js", "w")
  new.write("publications = [\n")
  for i in dir_list :
      addToMaster (path +'/'+i, new)
  new.write("];")

