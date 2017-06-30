# Runecsape accessing api

#!/usr/bin/python

import json, pprint
import webbrowser
import urllib.request
import codecs
import time
import datetime
import cycler
import matplotlib.pyplot as plt
import random

global base_url
global url
global database


randomdata = []

base_url = 'http://services.runescape.com/m=itemdb_oldschool'
lesser_url = '/api/catalogue/detail.json?item='
url = base_url+lesser_url

#convert the json file to a dict with item_ids as keys, and item names as values
with open('fullitemlist.json') as file:
     database = json.load(file)
new_database = {}
for item in database:
   name = item['id']
   new_database[name] = item['name']


#gets the price of an item based on the item's id
def get_price(item_id):
    with urllib.request.urlopen(url+item_id) as url:
        fulldata = json.loads(url.read().decode("utf-8"))
    return (fulldata['item']['current']['price'])    


#open the api page that has the item_id
def open_url():
    print("If item ID is unknown, enter 0")
    item_id = input('Enter item ID:')
    try:
        webbrowser.open(url+item_id)
    except:
        print("That item id does not exist!")
            
#get the id of an item
def get_item_from_id(item_id):
    try:
        return new_database[item_id]
    except:
        print('That item_id does not exist!')
        new_id = input("Input another item_id that exists:")
        return get_item_from_id(new_id)
            

# converts the second value of epoch time into a better value:
def convert_epoch_time(time):
#     newtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(key)))
    newtime = datetime.datetime.fromtimestamp(time)
    return newtime
    

def convert_dicts(database):
    new_database= {}
    for dict in database:
        new_database.update(database)
    return new_database

# 
# webbrowser.open(url)

# with urllib.request.urlopen(url) as url:
#     data = json.loads(url.read().decode("utf-8"))
# print(data) 
    # reader = codecs.getreader("utf-8")
    # data = json.load(reader(response)
# list = {}
# for value in database:
#     list.update(value)
# result = {}
# for d in database:
#    result.update
def make_graph(item_id):
    end_url = '/api/graph/'+str(item_id)+'.json'
    overall_url = base_url + end_url
    print(overall_url)
    with urllib.request.urlopen(overall_url) as url:
        try:
            graph_data = json.loads(url.read().decode("utf-8"))
        except:
            print('That item_id does not exist!')
            new_id = input("Input another item_id that exists:")
            return make_graph(new_id)
    # for key in graph_data["daily"]:
    #     key = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(key)))
    for key in graph_data["daily"]:
        plt.scatter(key, graph_data["daily"][key], c= 'b', marker ='o', linestyle = '-')
        plt.xlabel('Time(Epoch Seconds)')
        plt.ylabel('Value(gp)')
        plt.title('Historical Price data of'+' ' + new_database[item_id])
        plt.grid(True)
    plt.show()
  
  
  
if __name__ == "__main__":
    print('Hello World')
  
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    
    


