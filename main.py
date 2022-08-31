from serpapi import GoogleSearch
from functions import *
import time
import os


params = {
    "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
    "engine": "google_scholar_author",
    "author_id": "G1CnZ38AAAAJ",
    "hl": "en",
}

search = GoogleSearch(params)
results = search.get_dict()
for article in results['articles']:
    try:
        print (article)

        article_title = article['title']

        path = mkDir(article_title)

        link = querySearch(article_title)
        saveText("link",path,str(link))

        getAbstract(link,path)
        # savePdf(link,path)
        saveText ("authors",path,article['authors']) 
        saveText ("date",path,article['year']) 
    except: pass
    time.sleep(1)

