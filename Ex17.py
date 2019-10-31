#Exercise Question 6: Given a following two sets find the intersection and remove those elements from the first set
#First Set  {65, 42, 78, 83, 23, 57, 29}
#Second Set  {67, 73, 43, 48, 83, 57, 29}
#Intersection is  {57, 83, 29}
#First Set after removing common element  {65, 42, 78, 23}

import sys
#tset=set()
fset= {65, 42, 78, 83, 23, 57, 29}
sset= {67, 73, 43, 48, 83, 57, 29}
#tset.ad(fset&sset)
print(fset&sset)

for i in set(fset):
   if i in (fset&sset):
       fset.remove(i)
print(fset)



