#Exercise Question 9: Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
#sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5s
import sys
import re

def sumdigit(inputStr):
   sum=0
   avg=0
   count=0
   markList = [int(num) for num in re.findall(r'\b\d+\b', inputStr)]

   for mark in markList:
       sum+=mark
       count+=1
   avg=sum/count
   print("sum= ", sum, " avg= ", avg)
       
   
inputStr=input("enter a string: ")

sumdigit(inputStr)
