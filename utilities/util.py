from serpapi import GoogleSearch
import json
from utilities.dynamicArr import *
from utilities.classes import *
import requests
from bs4 import BeautifulSoup
import time
import random
import os

ignoreSym = "@ignore@"

def authorFormat(content : str):
    
    # For some reason it gets output with @cgiven@c: @c
    # content = content.replace("@cgiven@c: @c", '').strip()


    print(f"Authors are {content.split(',')}")
    prod = '@b[{'
    for i in content:
        if i == ',':
            prod += '@c},{'
        else:
            prod += i
    prod += '@c}]@b'
    return content

def getDate(content):
    lookItem = "Publication date"
    if lookItem not in content:
        return ignoreSym

    start = content.find(lookItem) + len(lookItem)
    content = content[start:]
    lookItem = 'gsc_oci_value">'
    start = content.find(lookItem) + len(lookItem)
    content = content[start:]
    end = content.find('<')
    date = content[:end].strip()

    if len(date) >= 4 and date[-4:].isdigit():
        year = date[-4:]
        return f'@b{{@cdate-parts@c:[[{year}]]}}@b'
    
    return content[:end]

def reduce(name):
    return name.split()[-1]

def getFull(search, input):
    if input not in search:
        return None
    endIndex = search.find(input) + len(input) - 1
    output = ""
    i = endIndex
    while i >= 0 and search[i] not in {',', '>'}:
        output = search[i] + output
        i -= 1
    return f"{output.strip()}"

def betterAuthNames(abname, content):
    names = abname.split(',')
    product = ""
    for i in names:
        lastN = reduce(i)
        extendedName = getFull(content, lastN)
        if extendedName is not None:
            product += extendedName + ', '
    return product[:-2]

def addToMaster(readFileName, FILE):
    if ".json" in readFileName:
        with open(readFileName, "r") as f:
            addition = f.read()
            if ignoreSym in addition:
                return
            addition = addition.replace(',{  ..."}', '')
            addition = addition.replace('@b"', '').replace('"@b', '')
            addition = addition.replace('@c', '"')
            FILE.write(addition + ",\n")

def getContent(url, auths):
    user_agent_list = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers)
    
    if r.status_code != 200:
        print(f"Request failed with status code {r.status_code}")
        return "found", "found", "found"

    soup = BeautifulSoup(r.content, 'html.parser')
    soup2 = BeautifulSoup(r.text, 'html.parser')
    
    searchItem = ">Authors</div><div class"
    startIndex = str(soup2).find(searchItem)
    forNames = str(soup2)[startIndex: startIndex + (len(auths.split(',')) * 25) + len(searchItem) * 3]
    results = str(soup)

    description = ""
    subs = ["OBJECTIVE", "BACKGROUND", "METHODS"]

    for sub in subs:
        startTarget = '"gsh_csp"'
        if startTarget not in results:
            startTarget = '"gsh_small"'
            if startTarget not in results:
                break

        endTarget = '</div>'
        start = results.find(startTarget) + len(startTarget)
        results = results[start:]
        end = results.find(endTarget)
        description += f"{sub}: {results[:end]}"

    return description, betterAuthNames(auths, forNames), getDate(str(soup2))

def divide(text):
    arr = DynamicArray()
    searchItem = "title"
    while searchItem in text:
        found = text.find(searchItem)
        arr.append(f"'title{text[:found]}")
        text = text[found + len(searchItem):]
    return arr
