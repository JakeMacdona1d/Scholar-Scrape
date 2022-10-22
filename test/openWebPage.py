import webbrowser
import os
import time

edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

webbrowser.get('edge').open('https://scholar.google.com/citations?view_op=view_citation&hl=en&user=G1CnZ38AAAAJ&citation_for_view=G1CnZ38AAAAJ:4JMBOYKVnBMC')

time.sleep(5)

os.system("taskkill /im msedge.exe /f")
