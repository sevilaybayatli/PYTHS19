#Exercise Question 8: Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
#rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
#sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#after removing unwanted elemnts from list [47, 69, 76, 97}

import sys
rollnum= [47, 64, 69, 37, 76, 83, 95, 97]
rollstr= ['Kelly', 'Jason', 'Emma']
sampleDict={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

#for i in rullnum:
#
 #      if (i in sampleDict.valuse()):
#          rullnum.pop(i)
#print(rullnum)

rollnum[:] = [item for item in rollnum if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollnum)
rollstr[:]=[item for item in rollstr if item in sampleDict.keys()] 
print("after removing unwanted elemnts from list ", rollstr)
     
         

