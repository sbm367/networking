#Test of urlib, specificly the requests module
import urllib.request

<<<<<<< HEAD
x = urllib.request.urlopen('https://www.google.com/')
=======
site = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'

x = urllib.request.urlopen(site)

>>>>>>> 9a9d02d930038331ea67c5d4911f6070310f1537
print(x.read())