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
import csv
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

def pull_time_data(start, start1):
    for item in range(start, start+10000):
        start1 = item
        if item in new_database:
            print(get_item_from_id(item))
            first = [get_item_from_id(item)]
            end_url = '/api/graph/'+str(item)+'.json'
            overall_url = base_url + end_url
            try:
                with urllib.request.urlopen(overall_url) as url:
                    data = json.loads(url.read().decode("utf-8"))
            except urllib.error.HTTPError as error:
                print("got blocked by website, waiting 1s")
                time.sleep(0.5)
                pull_time_data(start1+1, start1+1)
                # counter += 1
                # if counter >= 500:
                #     print("probably got ip banned by the site at item:" +str(item))
                #     return(item) 
                #     break
                # except:
                #     pass
            except json.decoder.JSONDecodeError:    
                print("Site wonky, waiting 1s")
                time.sleep(1)
                pull_time_data(start1+1, start1+1)
            newdata = data['average']
            
            
            
            newlist = list(newdata.values())
            newlist = first+newlist
            try:
                with open('historicaldata.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(newlist)
            except PermissionError as error:
                print("Close your Excel File!")
            except TypeError as error2:
                print("website has blocked us, waiting 120s")
                time.sleep(120)
                holder_index = i
                print(start1)
                return create_item_sheet(start1,start1)
  
if __name__ == "__main__":
    pull_time_data( 11105,11105)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    
    


