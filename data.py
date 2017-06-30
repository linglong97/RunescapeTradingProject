from apiscrape import new_database
import apiscrape
import json
import csv
import xlwt, xlsxwriter
import urllib
import time
import random
global dict, item_id, data

# dict is a dictionairy that returns the item name based on the id
dic = new_database
array = []

def function():
    global array
    if array == []:
        array = main()
    return array

# def get_item_name_from_id(name):
#     d2 = dict((v, k) for k, v in dic.iteritems())
#     try:
#         return d2[name]
#     except:
#         pass
#         
    
#adds data to the excel sheet
def create_item_sheet(dict):
    for i in range(0, 10000):
        try:
            print(exp_item_data(i))
            with open('name.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for element in exp_item_data(i):
                    writer.writerow([data])
        except:
            continue
        # except:   
        #     print('item_id'+ ' '+str(i)+' does not exist' )
        #     continue
       
            
        
#creates a list to be added into csv file
def create_item_data_full(array):
    for key in dict:
        print(exp_item_data(key))
        array.append(exp_item_data(key))
        time.sleep(random.randrange(0,1))
        
            
   
#     
# while 1:
#     newlist = []
#     for key in dict:
#         
#         with open('name.csv', 'a', newline='') as csvfile:
#                 writer = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#                 writer.writerow(['']*7+[key])
            
        
  


#given an item, reformats the json file into an dict so that it is easier to export
def exp_item_data(item_id):
    base_url = 'http://services.runescape.com/m=itemdb_oldschool'
    lesser_url = '/api/catalogue/detail.json?item='
    fullurl = base_url+lesser_url+str(item_id)
    itemdata = []  #Name, Price, Members, 30day, 90day, 180day trend
    holddata=[]
    with urllib.request.urlopen(fullurl) as url:
        try:
            holddata = json.loads(url.read().decode("utf-8"))
        except:
            pass
    itemdata.append(holddata['item']['name'])        
    itemdata.append(holddata['item']['current']['price'])
    itemdata.append(holddata['item']['members'])
    itemdata.append(holddata['item']['day30']['change'])
    itemdata.append(holddata['item']['day90']['change'])
    itemdata.append(holddata['item']['day180']['change'])
    return itemdata


def historical_data_export(item_id):
    pass
    
create_item_sheet(dict)


