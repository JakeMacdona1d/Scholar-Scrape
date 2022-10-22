abname = " j Smith, A Bro, Y Feaster, D baby"
authors = 'Abby Bro, John Smith, Yvon Feaster'


def reduce (name) :
    while not name.find(' ') == -1 :
        name = name[name.find(' ')+1:]
    return name


def getFull (search, input) :
    if str(search).find(input) == -1 : return None
    endIndex = str(search).find(input) + len(input) -1

    output = ""
    i = endIndex
    while not (search[i] == ',' or i < 0) :
        output = search[i] + output
        i -= 1
    return output.strip()

def betterAuthNames(abname, content) :
    names = abname.split(',')
    print (names)
    product = ""
    for i in names :
        lastN = reduce(i)
        extendedName = getFull(content, lastN)
        if extendedName == None :
            product += i + ', '
        else : product += (getFull(content, lastN)) + ', '

    product = product [:len(product)-2]
    return product

print (betterAuthNames(abname, authors))