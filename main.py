#Jake Macdonald
# Designed to produce json files with details of all articles authored by choice person.
#Retrives title, authors, url, and description

from util import *
import os.path


def main () :
  params = {
    "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
      "engine": "google_scholar_author",
      "author_id": "G1CnZ38AAAAJ",
      "hl": "en",
      "sort": "pubdate",
      "num": "100",
      "start": "0",
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
    sizeOffName = len(fName)
    if not sizeOffName :
      fName = item.authors 
      sizeOffName = len (fName)
    if sizeOffName > 15:
      fName = fName[:15]

    fName = fName.replace('"',"")
    fName = fName.replace('/',"")
    fName = fName.replace(' ',"")
    fName += str(sizeOffName)

    print ('datCache/ ' + fName +'.json')


    try:
      with open('datCache/ ' + fName +'.json', 'w') as json_file:
        print ("woag")
        continue
        # Do something with the file
    except IOError:
        print("File not accessible")
    finally:
        json_file.close()

   
    
    baseTime = 10.0
    time.sleep(baseTime + (baseTime * random.random()))

    item.abstract = getAbstract(str(item.link)) 
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

main()
