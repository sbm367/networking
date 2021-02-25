import urllib.request, urllib.parse, urllib.error
import json

service_url='https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter a location: ')
    if len(address) < 1 : break

    url = service_url + urllib.parse.urlencode({'address':address})

    print('Retrieving ',url)
    url_handler = urllib.request.urlopen(url)
    data = url_handler.read().decode()
    print('Retrived',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print(js)
