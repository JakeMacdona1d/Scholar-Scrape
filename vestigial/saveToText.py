def saveText (fileName,dir,content) :
    fileName = "authors.txt"
    text_file = open(dir + '/' + fileName, "w")
    n = text_file.write(content)
    text_file.close()


