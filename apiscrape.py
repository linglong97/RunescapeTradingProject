# Runecsape accessing api

import json, pprint
import webbrowser
import urllib.request
import codecs



base_url = 'http://services.runescape.com/m=itemdb_oldschool'+ '/api/catalogue/detail.json?item='


print("If item ID is unknown, enter 0")
item_id = input('Enter item ID:')

url = base_url+item_id

webbrowser.open(base_url+item_id)
with urllib.request.urlopen(base_url+item_id) as url:
    data = json.loads(url.read().decode("utf-8"))
    print(data)
    
    
    # reader = codecs.getreader("utf-8")
    # data = json.load(reader(response))



with open('objects_87.json.json') as file:
    database = json.load(file)



