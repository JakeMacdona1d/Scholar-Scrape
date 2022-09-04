#Jake Macdonald
# Designed to produce json files with details of all articles authored by choice person.
#Retrives title, authors, url, and description

from util import *

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
    time.sleep(10)
    item = ArtItem
    item.setTit(item,strArr[i])
    item.setLink(item,strArr[i])
    item.setAuth(item,strArr[i])
    print (item.link)
    item.abstract = getAbstract(str(item.link)) 
    if item.abstract == 'found' : return

    dictPort = {
      'title' : item.title, 
      'authors' : item.authors,
      'link' : item.link,
      'abstract' : item.abstract
    }
    title = item.title

    sizeOfTitle = len(title)
    if not sizeOfTitle :
      title = item.authors 
      sizeOfTitle = len (title)

    if sizeOfTitle > 15:
      title = title[:15]
    
    title = title.replace('"',"")
    title = title.replace('/',"")
    title = title.replace(' ',"")
    title += str(sizeOfTitle)

    with open('datCache/ ' + title +'.json', 'w') as json_file:
      json.dump(dictPort, json_file)  

main()
