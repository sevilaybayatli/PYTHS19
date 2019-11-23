import sys
#Write a Python program to check if a number is positive, negative or zero.

num=int(input("enter a number "))
if (num>0):
   print("the number is greather than zero")
elif(num<0):
   print("the number is less than zero")
else:
   print("the number is equal to zero")

my_list=[30,150,220,340,100]

divisable=list(filter(lambda x:(x%15==0),my_list))
print("Numbers divisible by 15 are",divisable)


