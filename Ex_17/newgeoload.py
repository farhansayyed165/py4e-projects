import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

conn= sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS locations(address TEXT, geodata TEXT)')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open('where.data.txt')
count = 0
for line in fh:
    if count > 20:
        print('Retrieved 200 locations, please start again')
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM locations WHERE address = ?", (memoryview(address.encode()),))

    try:
        data = cur.fetchone()[0]
        print('Found in database', address)
        continue
    except:
        pass
    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving url', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n',' '))
    count = count + 1

    try:
        js = js.loads(data)
    except:
        print(data)
        continue
    if "status" not in js or (js['status'] != OK and js['status'] != ' ZERO_RESULTS'):
        print('FALIURE TO Retrieve')
        print(data)
        break
    cur.execute('''INSERT INTO locations(address, geodata) VALUES(?,?)''', (memoryview(address.encode()),))
    conn.commit()
    if count % 10 == 0:
        print('Pausing for a bit....')
        time.sleep(2)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
