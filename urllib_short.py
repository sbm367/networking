import urllib.request, urllib.parse, urllib.error

url = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(url)
#optional param in url open to preserve headers
for line in fhand:
  print ( line.decode().strip() )

  counts = dict()
  for line in fhand:
    words = line.decode().split()
    for word in words:
      counts[word] = counts.get(word,0)+1
print(counts)