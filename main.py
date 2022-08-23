from serpapi import GoogleSearch
from functions import *

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
    # path = mkDir(article_title)

    article_link = article['link']
    # getAbstract(article_link,path)

    article_authors = article['authors']
    article_year = article['year']

    print ('\n')
    # print(f"Title: {article_title}\nLink: {article_link}\nAuthors: {article_authors}\nPublication: {article_year}\n")

