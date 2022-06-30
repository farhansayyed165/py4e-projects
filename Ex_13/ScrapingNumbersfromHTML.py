

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


sum = 0
list = list()
tags = soup('span')
for tag in tags:
    tag = str(tag)
    x = re.findall('[0-9]+', tag)
    for i in x:
        i = int(i)
        sum = sum+i

print('Count', sum)
