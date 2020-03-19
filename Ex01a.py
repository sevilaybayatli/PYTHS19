import sys
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a birth day name: (or enter blank for quite)')
    name=input()
    if name==' ':
       break
    if name in birthdays:
       print(birthdays[name], 'is the birthday ', name)
    else:
       print('Enter the birthday of ', name)
       bday=input()
       birthdays[name]=bday
       print('birthdays database updated')
