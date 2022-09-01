from requests_html import HTMLSession
import json

session = HTMLSession()
response = session.get('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=vicia+faba&btnG=')

# https://requests-html.kennethreitz.org/#javascript-support
response.html.render()

results = []

# Container where data we need is located
for result in response.html.find('.gs_ri'):
    title = result.find('.gs_rt', first = True).text
    # print(title)
    
    # converting dict of URLs to strings (see how it will be without next() iter())
    url = next(iter(result.absolute_links))
    # print(url)

    results.append({
        'title': title,
        'url': url,
    })

print(json.dumps(results, indent = 2, ensure_ascii = False))