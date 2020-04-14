# lucky
# run from terminal: python lucky.py
# currently there's a bug in vscode code-runner

import requests, sys, webbrowser
import bs4

search_term = 'sabbu ripposte'

print('Giggling...') # display while searching
res = requests.get('http://google.com/search?q={0}'.format(search_term), 'lxml')
res.raise_for_status()

# Retrieve top searches
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # webbrowser.open('http://google.com' + linkElems[i].get('href'))
    webbrowser.get('chrome %s').open_new_tab('http://www.google.com' + linkElems[i].get('href'))
