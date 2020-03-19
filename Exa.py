import sys

#def eggs(newParameter):
#    newParameter.append('Hello')

#spam=[1,2,3]
#eggs(spam)
#print(spam)
#the function would return 'apples, bananas, tofu, and cats'
lls=[]
def boncu(npara):
    nlist=''
    for i in npara:
        if i=='cats':
           nlist=nlist+'and '+i
        else:
           nlist=nlist+i+', '
    lls.append(nlist)
    return lls
     



spam = ['apples', 'bananas', 'tofu', 'cats']

print(boncu(spam))
