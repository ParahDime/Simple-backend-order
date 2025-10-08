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

#obtains the quantity of the items, as well as the average per order as well
def totalQuant(product_orders):
    totals = {}
    for product, orders in product_orders.items():
        total_qty = sum(order.quantity for order in orders)
        count = len(orders)
        avg = total_qty / count #if count > 0 else 0
        totals[product] = {"total": total_qty, "average": avg}

    return totals

def isHotSeller(product_orders):
    pass

#merge sort algorithm
def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Compare totals — descending order
        if left[i][1]["total"] >= right[j][1]["total"]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list



#initialise variables
items = ['apple', 'banana', 'orange', 'grape', 'pepper', 'plum', 'strawberry', 'pineapple', 'apricot']
genItems = random.randint(5, 25)
orders = [] #ledger of orders
product_orders = {} #hashmap, summary
order_queue = deque() #for processing orders
orderProcessed = 0

for item in range(genItems):
    fruit = random.choice(items)
    quantity = random.randint(1, 10)
    timestamp = int(time.time()) + item
    
    new_order = createOrder(item + 1, fruit, quantity, timestamp) 
    orders.append(new_order)

    if fruit not in product_orders:
        product_orders[fruit] = []
        product_orders[fruit].append(new_order)
    else: #if fruit already there
        product_orders[fruit].append(new_order)

    order_queue.append(new_order)

    print("Order " + str(item + 1) + ": " + str(quantity) + " " + str(fruit) + " added to the list.")

del items

for item in range(genItems):
    print(f"Processing order: {order_queue[item].id}")
    orderProcessed = orderProcessed + 1
    #order_queue.popleft()
    pass

totals = totalQuant(product_orders) #find the highest amount of each item
items_list = list(totals.items())
new_totals = merge_sort(items_list)#sort the list from high to low
totals = dict(new_totals)

del items_list
del new_totals
print("Top Products by quantity:")
for key, value in list(totals.items())[:3]:
    print(f"{key}: {totals[key]['total']} ")
    pass

hotSells = isHotSeller(product_orders)
print("Hot sellers:")
for x in range(3):
    #print top 3 sellers
    pass
del hotSells

print("Average order quantity over assigned period:")
for key in totals:
    print(f"{key}: {totals[key]['average']} ")
    pass

del totals

#account for all items processed
print("Total orders processed: " + str(orderProcessed))

del orderProcessed