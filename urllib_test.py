#Test of urlib, specificly the requests module
import urllib.request

site = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'

x = urllib.request.urlopen(site)

print(x.read())