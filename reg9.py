import re

#Write a Python program to find the substrings within a string.
#Sample text :'Python exercises, PHP exercises, C# exercises'
#Pattern :'exercises'
#Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
text= 'Everything will be fine soon 1234 Read and it is goining to be nice 12'

pattern="Read"

z=re.search(pattern, text)
print(z.group(0))
patt="Read"

s=re.sub("R\w+","Rd\.",patt)
print(s)

# Write a Python program to separate and print the numbers and their position of a given string.
#text= 'Everything will be fine soon 1234 and it is goining to be nice 12'
#for element in re.finditer("\d+",text):
#    print(element.group(0))
#    print("Index Position= ", element.start())
     
    


#Write a Python program to find all words starting with 'a' or 'e' in a given string.
#text= 'Everything awill be afine soon 1234 and it is goining to be nice 12'

#m=re.findall("ae\w+", text)
#print(m)


#Write a Python program to separate and print the numbers of a given string.
#text= 'Everything will be fine soon 1234 and it is goining to be nice 12'
#result=re.split("\d+",text)
#for element in result:
   # print(element)
       

#Write a Python program to match if two words from a list of words starting with letter 'P'
# Sample strings.
#words = ["Python PHP", "Java JavaScript", "c c++"]

#for w in words:
#        m = re.match("(P\w+)\W(P\w+)", w)
#        # Check for success
#        if m:
#            print(m.groups())


#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
#def subst(url):
#     return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', url)
     

#url='2016-09-02'
#print(subst(url))

#Write a Python program to extract year, month and date from a an url.
#def findDate(url):
#    return re.findall(r'\d{4}/\d{1,2}/\d{1,2}',url)
#url= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
#print(findDate(url))

#Write a Python program to replace whitespaces with an underscore and vice versa.
#text='Ali_albazi has four cats'
#match= re.sub(r'[_]', ' ', text)
#print(match)
#match= text.replace(' ', '_')
#print(match)
#text='Python exercises, PHP exercises, C# exercises'
#pattern = 'exercises'


#Write a Python program to find the occurrence and position of the substrings within a string.
#for match in re.finditer(pattern,text):
    #s=match.start()
     #e=match.end()
     #print('Found "%s" at %d:%d' % (text[s:e], s, e))

