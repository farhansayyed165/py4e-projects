import json
import urllib.request, urllib.parse, urllib.error
import ssl

count = 0
total = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter url -')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
info = json.loads(data)


for item in info["comments"]:
    count = count + 1
    t = int(item["count"])
    total = total + t


print('Count: ', count)
print('Sum: ', total)
