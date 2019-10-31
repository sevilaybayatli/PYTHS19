#Exercise Question 4: Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
#Origigal list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
#Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

import sys

origList= [11, 45, 8, 11, 23, 45, 23, 45, 89]
countDict=dict()
for i in origList:
    countDict[i]=origList.count(i)
print(countDict)
    
