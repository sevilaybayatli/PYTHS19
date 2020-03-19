# "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

import sys
from datetime import datetime
from datetime import date
import calendar
print("Twinkle, twinkle, little star")
print("        How I wonder what you are!")
print("              Up above the world so high")
print("              Like a diamond in the sky")
print("Twinkle, twinkle, little star")
print("         How I wonder what you are")
print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))

now= datetime.now()
d1=now.strftime("%d/%m/%y %H:%M:%S")
print(d1)

#radis=float(input("enter the radious of circle: "))

#area=3.14*radis*radis
#print("the area of circle= ", area)

#fname=input("enter the first name: ")
#sname=input("enter the second name: ")
#print("the name= ", sname, "", fname)

#numbers= input("numbers= ")
#number=numbers.split(",")
#print(numbers)
#tup=tuple(numbers)
#print(tup)

#file_name=input("enter file name: ")
#f_extns=file_name.split(".")
#print(f_extns)
#print("the extension of file is: ", f_extns[-1])

#color_list = ["Red","Green","White" ,"Black"]
#print("first color= ",color_list[0], "second color= ", color_list[-1])

exam_st_date = (11, 12, 2014)
print("the exam start date is %i/ %i/ %i"%exam_st_date)

#n=int(input("enter the number: "))
#n1=int("%s" %n)
#n2=int("%s%s" % (n,n))
#n3=int("%s%s%s" %(n,n,n))
#print(n1+n2+n3)
print(abs.__doc__)

#m=int(input("enter month: "))
#y=int(input("enter year: "))
#print(calendar.month(y, m))
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")
f_date=date(2014, 7, 2)
s_date=date(2014, 7, 11)
n=s_date - f_date
print(n.days)

r=6
vol=(3/4)*3.14*(r*r*r)
print("the volume of sphare= ", vol)









