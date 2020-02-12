import sys
catnames=[]

while True:
   print('Enter the name of cats '+ str(len(catnames)+1)+ '(neter nothing to stop)')

   name=input()
   catnames=catnames+[name]
   if name== '':
     break
print('name of cats ')
for n in catnames:
   print(' '+n)
