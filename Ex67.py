import sys
import math
import matplotlib.pyplot as plt 

##def histogram(items):
#    for n in items:
#        output=''
#        times=n
#        while times>0:
#            output+='@'
#            times-=1
#        print(output)
        
#histogram([9,2,4,5,3])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to concatenate all elements in a list into a string and return it
#def concatenate(lisst):
 #  stringg=''
 #  for n in lisst:
  #     stringg+=n
   #print(stringg)



#ll=input("enter the list of letters: ")
#lisst=ll.split(",")
#concatenate(lisst)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
#numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
 #   ]

#def printing(numbers):
#     for n in numbers:
#         if n==237:
#            print(n)
#            break;
 #        elif (n%2==0):
 #           print(n)
#numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]

#printing(numbers)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
#def colorlist(tset):
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
   
#   for n in color_list_1:
 #      if n not in color_list_2:
 #          tset.append(n)
#tset=set()
#print(color_list_1.difference(color_list_2))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

#def gcd(x, y):
#    gcd = 1
    
 #   if x % y == 0:
 #       return y
    
 #   for k in range(int(y / 2), 0, -1):
 #       if x % k == 0 and y % k == 0:
 #           gcd = k
 #           break  
 #   return gcd

#print(gcd(12, 17))
#print(gcd(4, 6))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to get the least common multiple (LCM) of two positive integers.
#def lcd(x,y):
 #  if x>y:
#     z=x
#   else:
 #    z=y
  # while(True):
   #   if (z%x==0 and z%y==0):
    #     lcd=z
     #    return lcd
      #z+=1



#print(lcd(4,6))
#print(lcd(15,17))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
#x=int(input("enter a n1"))
#y=int(input("enter a n2"))
#z=int(input("enter a n3"))

#k=0

#if (x==y or x==z or y==z):
#    k=x+y+z
#    k=0
#    print(k)

#else:
#  print(x+y+z)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

#def summ(x,y):
#     z=x+y
 #    if z in range (15,20):
#          sum=20
 #         return sum
 #    else:
 #         return z
     

#x=int(input("enter a number: "))
#y=int(input("enter a number: "))

#print(summ(x,y))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def values(x,y):
     z=x+y
     k=x-y
     if (x==y or z==5 or k==5):
          return True

x=int(input("enter a number: "))
y=int(input("enter a number: "))

print(values(x,y))





         
