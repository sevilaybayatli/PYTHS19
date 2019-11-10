# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
import sys
#ss=[]
#def listtuple(I):
 #   for i in (I):
 #      ss.append(i)
    
        

x=input("enter numbers: ")
I= x.split(",")
t=tuple(I)
print(I)
print (t)
