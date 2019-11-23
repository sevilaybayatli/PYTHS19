import sys
import glob
#Write a Python program to make file lists from current directory using a wildcard.
file_list=glob.glob('*.*')
print(file_list)
#Write a Python program to remove the first item from a specified list. 
for i in file_list:
    file_list.remove(i)
    break;
print(file_list)
