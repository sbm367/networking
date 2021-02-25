import json

# dictionary example
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type":"intl",
        "number":"+1 734 303 4456"   
    },
    "email" : {
        "hide":"yes"
    }
}
'''
# loads vs load means load from string
info = json.loads(data)
print('Name : ', info['name'])
print('Hide? : ', info['email']['hide'])

# list example
data2 = '''
[
   {
       "id" : "001",
       "x" : "2",
       "name" : "Chuck"
   },
   {
       "id" : "009",
       "x" : "7",
       "name" : "Charles"
   }
]
'''

info2 = json.loads(data2)
print('User count : ', len(info2))


for user in info2:
    print("\n User data")
    for key in user.keys():
        print(key, ":", user[key])