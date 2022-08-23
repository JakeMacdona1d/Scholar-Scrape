from serpapi import GoogleSearch
from functions import *
import time

params = {
    "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3",
    "engine": "google_scholar_author",
    "author_id": "ggHXV-4AAAAJ",
    "hl": "en",
}

search = GoogleSearch(params)
results = search.get_dict()
for article in results['articles']:
    print (article)

    article_title = article['title']

    path = mkDir(article_title)

    link = querySearch(article_title)

    getAbstract(link,path)
    savePdf(link,path)
    saveText ("authors",path,article['authors']) 
    saveText ("date",path,article['year']) 

    time.sleep(15)

