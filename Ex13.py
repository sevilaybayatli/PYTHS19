#Exercise Question 3: Given a list slice it into a 3 equal chunks and rever each list
#Origigal list  [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Chunk  1 [11, 45, 8]
#After reversing it  [8, 45, 11]
#Chunk  2 [23, 14, 12]
#After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
#After reversing it  [89, 45, 78]

import sys
#%%%%%%%%%%%%%%%%%first solution%%%%%%%%%%%%%%%%%%%%%%%
#sList=[11, 45, 8, 23, 14, 12, 78, 45, 89]
#L1=[]
#L2=[]
#L3=[]
#for i in sList[0:3]:
#     L1.append(i)
#     L1.reverse()
#print(L1)

#for j in sList[3:6]:
#     L2.append(j)
#     L2.reverse()
#print(L2)

#for k in sList[6:9]:
#    L3.append(k)
#    L3.reverse()
#print(L3)

#%%%%%%%%%%%%%%%%%second solution%%%%%%%%%%%%%%%%%%%%%%%%
sList=[11, 45, 8, 23, 14, 12, 78, 45, 89]

length=len(sList)
chunksize=int(length/3)
start=0
end=chunksize

for  i in  range(1,4,1):
    indexes=slice(start,end,1)
    listchunk=sList[indexes]

    print("after reversing it: ", list(reversed(listchunk)))
    start=end
    if(i!=2):
      end+=chunksize
    else:
      end+=length-chunksize

      
      






    
    
 
    
