from util import *


params = {
  "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
    "engine": "google_scholar_author",
    "author_id": "G1CnZ38AAAAJ",
    "hl": "en",
}

search = GoogleSearch(params)
results = dict(search.get_dict())
first = str(results.get('articles'))


# articles = DynamicArray ()
strArr = divide(first)
for i in range(len(strArr)) :
  time.sleep(1)
  item = ArtItem
  item.setTit(item,strArr[i])
  item.setLink(item,strArr[i])
  item.setAuth(item,strArr[i])
  item.abstract = getAbstract(item.link)
  # articles.append(item)

  dictPort = {
    'title' : item.title, 
    'authors' : item.authors,
    'link' : item.link,
    'abstract' : item.abstract
  }

  with open(item.title+'.json', 'w') as json_file:
    json.dump(dictPort, json_file)
