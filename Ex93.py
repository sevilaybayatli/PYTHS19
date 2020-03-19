import sys
string_maps = {"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"}
#a=str(a)
#b=str(b)
#for i in string_maps:
#for j in string_maps["1"]:
#   for k in string_maps["2"]:
#       print(j+k)
a=3
b=4
print("a add b= ", sum([a,b]))

def combination(a, b):
   a = str(a)
   b = str(b)
   for x in string_maps[a]:
      for z in string_maps[b]:
           print(x+z)

combination(2,3)
