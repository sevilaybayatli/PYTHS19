import sys
l=[1,4,7,3]

def maxmins (l):
  z=l[0]
  for i in l:
     
     if i > z:
        z=i
  return z

print(maxmins(l))
