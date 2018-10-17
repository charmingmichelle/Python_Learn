from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

taglist=list()

for i in range(count):
    print ("Retrieving:",url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    for tag in tags:
        taglist.append(tag)
    url = taglist[position-1].get('href', None)
    del taglist[:]
print ("Retrieving:",url)
