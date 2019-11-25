import sys
#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other. 

def distinct_data(data):
    if (len(data)==len(set(data))):
        return True
    else:
        return False;

print(distinct_data([1,2,3,4,5]))
print(distinct_data([1,5,6,5,7]))
