import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com'

response = requests.get(url)

html_file = BeautifulSoup(response.text, "html.parser")

print(html_file.prettify())