import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

cp = 0
i = 0
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
urlcount = int(input('Enter count:'))
urlposition = int(input('Enter position:'))
tagslist = []

import re

for x in range(0, urlcount):
    tags = soup('a')
    mytags = tags[urlposition-1]
    needed_tag = mytags.get('href', None)
    url = str(needed_tag)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(mytags.get('href', None))
