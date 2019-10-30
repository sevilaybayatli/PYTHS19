#Exercise Question 8: Find all occurrences of “USA” in given string ignoring the case
#input_str = "Welcome to USA. usa awesome, isn't it?"
#The USA count is: 2

import sys
inputStr= "Welcome to USA USA. usa usa awesome, isn't it?"
words=inputStr.split()

count=0

for string in words:
   if(string=='usa'):
      count+=1
   if (string=='USA'):
      count+=1
    
      
print("the number of usa or USA in input string: ", count)






