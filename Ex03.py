#"Accept string from the user and display only those characters which are present at an even index"
import sys

def strin(sst):
   #ttr=int(sst)
   for i in range(0, len(sst), 2):
       
       print("indix[",i,"]", sst[i])


st= input("enter string: ")


strin(st)

   

