#Exercise Question 5: Given a two list of equal size create a set such that it shows the element from both lists in the pair
#First List  [2, 3, 4, 5, 6, 7, 8]
#Second List  [4, 9, 16, 25, 36, 49, 64]
#Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

import sys
fList=[2, 3, 4, 5, 6, 7, 8]
sList=[4, 9, 16, 25, 36, 49, 64]

listresult=zip(fList,sList)
result=set(listresult)
print(result)
    
