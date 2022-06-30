from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter:')
if len(url)<1: url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('tr')
lst = list()
sum = 0
import re
for tag in tags:
    strtag = str(tag)
    num = re.findall("[0-9]+", strtag)
    print(num)
    if len(num)<1: continue
    for x in num:
        i = int(i)
        sum = sum+i

print(sum)
