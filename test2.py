from serpapi import GoogleSearch

params = {
  "engine": "google_scholar",
  "cluster": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:maZDTaKrznsC",
    "api_key": "c801fb0ffe9a68445624b9e9c7bd2d0a84bbc0bd9db4506cf91f267b8b3f44f3", #os.environ['serapapiKey'],
}

search = GoogleSearch(params)
results = search.get_dict()
print (results)