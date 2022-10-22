# container for elements of Google Scholar articles 
class ArtItem:
    title = "'title': '"
    link = "'link': '"
    authors = "'authors': '"
    abstract = ""
    date = ""

    def setLink (self,text):
      text = text.replace('"',"'") #needed b/c inconsistent html formats
      searchStartItem = "'link': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.link = text[start:end + start]
      self.link = str(self.link).replace("'",'')
      self.link = str(self.link).replace('link: ','')

    def setTit (self,text):
      text = text.replace('"',"'")
      searchStartItem = "'title': "
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.title = text[start:end + start]
      self.title = str(self.title).replace("'",'')
      self.title = str(self.title).replace("title: ",'')

    
    def setAuth (self,text):
      text = text.replace('"',"'")
      searchStartItem = "'authors': '"
      searchEndItem = "', '"
      start = text.find (searchStartItem) 
      end = text[start:].find (searchEndItem)
      self.authors = text[start:end + start]
      self.authors = str(self.authors).replace("'",'')
      self.authors = str(self.authors).replace("authors: ",'')