import sys
#Stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger':1, 'arrow': 12}
#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#def displayInventory(Inventory):
#   totalItem=0
 #  for k,v in Inventory.items():
  #      print(str(v)+' '+ k)
  #      totalItem=totalItem+v
  # print('the total items = '+ str(totalItem))
#displayInventory(Stuff)
#inv = {'gold coin': 42, 'rope': 1}
#dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#def addToInventory(inventory, addedItems):
 # for item in dragonLoot:
 #     inv.setdefault(item,[])
  #for k, v in inv.items():
  #    print(k+ ' '+str(v) )

#addToInventory(inv, dragonLoot)      


#inv = addToInventory(inv, dragonLoot)
#displayInventory(inv)
dict = {'gold coin': 42, 'rope': 1}
list = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
    for item in list:
        dict.setdefault(item, 0)
        dict[item] = dict[item] + 1

def displayInventory(inventory):
    print('Inventory:')
    itemCount = 0
    for k, v in inventory.items():
       print(str(v) + ' ' + k)
       itemCount=itemCount+v
    print('Total number of items: ' + str(itemCount))

newInventory=addToInventory(dict, list)
displayInventory(dict)


