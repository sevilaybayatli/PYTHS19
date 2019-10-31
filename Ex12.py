#Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
# Origigal list  [34, 54, 67, 89, 11, 43, 94]
# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

import sys

origList= [34, 54, 67, 89, 11, 43, 94]
z=origList.pop(4)
print(origList, z)

origList.insert(2,z)
print(origList)
origList.append(z)
print(origList)

