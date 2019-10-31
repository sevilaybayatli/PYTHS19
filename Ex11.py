# Exercise Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

import sys

listOne=[3, 6, 9, 12, 15, 18, 21]
listTwo=[4, 8, 12, 16, 20, 24, 28]
thirdList=[]

for i in listOne:
   if ((listOne.index(i))%2!=0):
      thirdList.append(i)

for j in listTwo:
    if (((listTwo.index(j))%2)==0):
       thirdList.append(j)
print(thirdList)
      
