#Exercise Question 10: Remove duplicate from a list and create a tuple and find the minimum and maximum number
#sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
#unique items [87, 45, 41, 65, 99]
#tuple (87, 45, 41, 65, 99)
#min: 41
#max: 99

import sys
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
uniqlist=[]
#ntuple=()
for item in sampleList:
    if item not in uniqlist:
       uniqlist.append(item)
ntuple=tuple(uniqlist)

print(ntuple)
print("Minimum number is: ", min(ntuple))
print("Maximum number is: ", max(ntuple))

