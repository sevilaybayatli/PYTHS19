import sys
def printTable(itemList):
    colWidths = [0] * len(tableData) # which will create a list containing the same number of 0 values as the number of inner lists in tableData .
    colWidth=[]
    longest=0
    word= ' '
    for i in itemList:
        for j in i:
            if len(j)>longest:
               word=j
               longest=len(j) 
        colWidth.append(word)
        word=' '
        longest=0
    #for item in colWidth:
        #print(item)
    for i in itemList:
        for j in i:
           print(j.rjust(len)

tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']] 

print(printTable(tableData))

