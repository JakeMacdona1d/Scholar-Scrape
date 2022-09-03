from util import *


params = {
  "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
    "engine": "google_scholar_author",
    "author_id": "G1CnZ38AAAAJ",
    "hl": "en",
    "sort": "pubdate",
    "num": "100",
    "start": "60",
}

search = GoogleSearch(params)
results = dict(search.get_dict())
first = str(results.get('articles'))


# articles = DynamicArray ()
strArr = divide(first)
for i in range(len(strArr)) :
  if i == 0  : continue #b/c weirdness of ds
  time.sleep(10)
  item = ArtItem
  item.setTit(item,strArr[i])
  item.setLink(item,strArr[i])
  item.setAuth(item,strArr[i])
  print (item.link)
  item.abstract = getAbstract(str(item.link)) 

  dictPort = {
    'title' : item.title, 
    'authors' : item.authors,
    'link' : item.link,
    'abstract' : item.abstract
  }
  title = item.title

  if len(title) > 15:
    title = title[:15]

  title = title.replace('"',"")
  title = title.replace('/',"")

  with open('jsonCache/ ' + title +'.json', 'w') as json_file:
    json.dump(dictPort, json_file)
