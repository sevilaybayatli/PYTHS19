import sys
def sumnu(num):
   previousnum=0

   for i in range(num):
       summ=previousnum+i
       print(summ)
       previousnum=i

print("print numbers in given range")

sumnu(10)
