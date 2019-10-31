#Exercise Question 7: Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set
#firstSet = {27, 43, 34}
#secondSet = {34, 93, 22, 27, 43, 53, 48}

#First set is subset of second set - True
#Second set is subset of First set -  False

#First set is Super set of second set -  False
#Second set is Super set of First set -  True

#First Set  set()
#Second Set  {67, 73, 43, 48, 83, 57, 29}

import sys
fset={27, 43, 34}
sset={34, 93, 22, 27, 43, 53, 48}
print("first set is :",fset)
print("second set is :", sset)

print("First set is subset of second set - ", fset.issubset(sset))
print("First set is subset of second set - ", sset.issubset(fset))

print("First set is Super set of second set -  ", fset.issuperset(sset))
print("Second set is Super set of First set -  ", sset.issuperset(fset))

if (fset.issubset(sset)):
    fset.clear()
print("first set",fset)

if(sset.issubset(fset)):
  secondSet.clear()

print("second set", sset)







