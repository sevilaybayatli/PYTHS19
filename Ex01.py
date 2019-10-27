#Question 10: Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list
#listOne = [10, 20, 23, 11, 17]
#listTwo = [13, 43, 24, 36, 12]
#Merged List is
#[23, 11, 17, 24, 36, 12]

import sys

def ssd():
   listOne = [10, 20, 23, 11, 17]
   listTwo = [13, 43, 24, 36, 12]
   listThird= [1]
   for i in listOne:
        if (i%2 != 0):
           listThird.append(i)
   for j in listTwo:
        if (j%2==0):
           listThird.append(j)
   return listThird
   #for k in listThird:
print(ssd(listOne, listTwo))


#def mergeList(listOne, listTwo):
 # thirdList = []
#  for num in listOne:
 #   if(num % 2 != 0):
 #     thirdList.append(num)
  #for num in listTwo:
   # if(num % 2 == 0):
    #  thirdList.append(num)
 # return thirdList
    
#print("Merged List is")
#listOne = [10, 20, 23, 11, 17]
#listTwo = [13, 43, 24, 36, 12]

#print(mergeList(listOne, listTwo))



   
           

