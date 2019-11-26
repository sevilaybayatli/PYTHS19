import sys
text='''The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.'''
ptext=text.replace(" ","")
print(ptext)
#pptext=ptext.split()
#print(pptext)
letter_list=""
for i in ptext:
    letter_list+=i
letter_freq=[ptext.count(n) for n in ptext]

print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(letter_list, letter_freq)))))
