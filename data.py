from apiscrape import new_database
import apiscrape
import json
import csv
# import xlwt, xlsxwriter
import urllib
import time
import random
global dict, item_id, data

# dict is a dictionairy that returns the item name based on the id
dict = new_database
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
def create_item_sheet_various_data(starting_range, holder_index):
    counter = 0
    if starting_range >= 13191:
        print("Done going through entire dictionairy.")
    for i in range(starting_range, starting_range+10000):
        try:
            time.sleep(0.05)
            if i in dict:
                data = [i]+exp_item_data(i)
                with open('July2.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(data)
                    counter = 0
            holder_index = i

        except urllib.error.HTTPError as error:
            print("Item_id not an item:"+ str(i))
            counter += 1
            if counter >= 500:
                print("probably got ip banned by the site at item:" +str(i))
                return(i) 
                break
        except TypeError as error2:
            print("website has blocked us, waiting 120s")
            time.sleep(120)
            holder_index = i
            print(holder_index)
            return create_item_sheet(holder_index, holder_index)
        except PermissionError:
            print('Close your Excel file')
            return(i) 
            break
    # except TypeError as error2:
    #     print('Site has blocked us, waiting 5 seconds. Item_id =' + str(starting_range))
    #     time.sleep(random.randrange(5,10))
    #     return create_item_sheet(holder_index+1, holder_index+1)

        # except:   
        #     print('item_id'+ ' '+str(i)+' does not exist' )
        #     continue
       
            
        
#creates a list to be added into csv file
def create_item_data_full(array):
    for key in dict:
        print(exp_item_data(key))
        time.sleep(random.randrange(0,1))
        array.append(exp_item_data(key))
    

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

create_item_sheet(12296,12296)
track =12296



# global new_index
# new_index = 172
# running = True
# holder_index = 92
# while 1:
#     running = True
#     while running:
#         create_item_sheet(starting_range, holder_index)
#         # try:
#         #     holder_index= int(new_index)
#         # except TypeError:
#         #     new_index = holder_index 
#         # try:
#         #     new_index = create_item_sheet(new_index, holder_index)
#         # except:
#         #     new_index = create_item_sheet(holder_index+1,holder_index)
#         print('now waiting 5 seconds')
#         time.sleep(5)
#         running = False

