import xml.etree.ElementTree as et

data = '''
<people>

  <person>
    <name>Chuck</name>
    <phone type="intl">
      +1 734 303 4456
    </phone>
    <email hide="yes" />
  </person>

  <person>
    <name>Charles</name>
    <phone type="intl">
      +1 555 867 5309
    </phone>
    <email hide="yes" />
  </person>

</people>
'''

# This could blow up if there are syntax errs

#this is actually a pointer to the root node
tree = et.fromstring(data)
print('Tree :', tree)
print('Tree[0] :', tree[0])
print('Tree[0][0]:', tree[0][0])


print('Tag :', tree.tag)
print('Attributes :', tree.attrib)

for node in tree:
  print('node tag : ', node.tag)
  print('node attr : ', node.attrib)
  for node2 in node:
    print('node2 tag : ', node2.tag)
    print('node2 attr : ', node2.attrib)

print('\n')

# this isnt working for some reason
print('recursive enumeration')
for node in tree.iter('node'):
  print("This runs once")
  print(node.tag)
  print(node.attrib)


print('\n')

'''
root = tree.getroot()
print('Root :', root)
'''

print('Name : ', tree.find('name'))
print('Name : ', tree.find('name').text)
print('Attr : ', tree.find('email').get('hide'))

# Find all matches 
print('Tree :', tree)
lst = tree.findall('person')
print('List :', lst)
print('User Count : ', len(lst))

for item in lst:
  print(item)
  print('Name : ', item.find('name').text)

  '''
  print('Name : ', item)
  print('Phone : ', item.find('phone').text, 'Type : ', item.find('phone').get('type'))  
  '''
