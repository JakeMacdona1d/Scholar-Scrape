import requests
from bs4 import BeautifulSoup

url = 'https://scholar.google.com/citations?hl=en&user=G1CnZ38AAAAJ&view_op=list_works&sortby=pubdate'

response = requests.get(url)

html_file = BeautifulSoup(response.text, "html.parser")


print(html_file.prettify())

print (html_file.find('gsc_a_t'))
