import math
from numpy import random
from collections import deque
import time
#importing any classes
from order import order


#function for normalising string names
def normaliseString(fruit):
    fruit = fruit.lower()
    #check for whitespace
    #remove any duplicates
    return fruit
#function for creating orders
def createOrder(item, fruit, quantity, timestamp):
    fruit = normaliseString(fruit)
    newItem = order(item, fruit, quantity, timestamp)
    return newItem


def isHotSeller():
    pass



#initialise variables

items = ['apple', 'banana', 'orange', 'grape', 'pepper', 'plum', 'strawberry', 'pineapple', 'apricot']
genItems = random.randint(5, 25)
orders = [] #ledger of orders
product_orders = {} #hashmap, summary
order_queue = deque() #for processing orders

#populate orders
for item in range(genItems):
    fruit = random.choice(items)
    quantity = random.randint(1, 10)
    timestamp = int(time.time()) + item
    
    new_order = createOrder(item + 1, fruit, quantity, timestamp)
    
    orders.append(new_order)
    #input into a hash map
    if fruit not in product_orders:
        product_orders[fruit] = []
    else: #if fruit already there
        product_orders[fruit].append(new_order)

    #import into the deque
    order_queue.append(new_order)

    print("Order " + str(item + 1) + ": " + str(quantity) + " " + str(fruit) + " added to the list.")

for item in range(genItems):
    #process deque


    pass




