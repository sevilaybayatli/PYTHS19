# Question 7: Return the number of times that the string “Emma” appears anywhere in the given string
import sys

def count_jhon(statement):
  count = 0
  for i in range(len(statement)-1):
    count += statement[i:i+4] == 'Emma'
  return count

count = count_jhon("Emma is good developer. Emma is aslo a writer")
print("Emma appeared ", count, "times")
          
     

