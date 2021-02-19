#Test of urlib, specificly the requests module
import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())