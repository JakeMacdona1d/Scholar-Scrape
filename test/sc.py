import pyscreenshot as ImageGrab
import tkinter
import os
import time
import webbrowser


def openWebPage () :
    edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    webbrowser.get('edge').open('https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:4JMBOYKVnBMC')



def screenShot() :
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print (width/2)
    im=ImageGrab.grab(bbox=(int(width/2),0,width,height))
    im.save("thot/output.jpg")

    time.sleep(10)

    os.system("taskkill /im msedge.exe /f")

openWebPage()
screenShot()