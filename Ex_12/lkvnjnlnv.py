import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count: '))+1
position = int(input('Enter position: '))


tags = soup('a')
tags_lst = list()
for tag in tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)
for i in range(0,count):
    print ('retrieving: ',tags_lst[position])
    position = position + 1
