import sys
#days=int(input("enter a days"))*3600*24
#hours=int(input("enter a hours"))*3600
#minutes=int(input("enter a minutes"))*60
#seconds=int(input("enter a seconds"))
#time=days+hours+minutes+seconds
#print("the amounts of seconds: ", time)

#weight=int(input("enter your weight in kilogram: "))
#hight=int(input("enter your hight in cm "))

#print("your mass data is ", round(weight/(hight*hight),2))
#aa=[6,5,8,1,2]
#sum=0
#for i in aa:
#   sum+=i
#print("the sum of digits=", sum)
#Write a Python program to sort three integers without using conditional statements and loops.
a1=int(input("enter a first number: "))
a2=int(input("enter a second number: "))
a3=int(input("enter a third number: "))

x=max(a1,a2,a3)
z=min(a1,a2,a3)

y=(a1+a2+a3)-x-z
print("the sorted numbers: ", x,y,z )
