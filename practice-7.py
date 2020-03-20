#! python 3
import re
#1-What is the function that creates Regex objects?
##regexObject=re.compile(r'blabla')

#2-2. Why are raw strings often used when creating Regex objects?
#3. What does the search() method return? retrun first much of values 
#4. How do you get the actual strings that match the pattern from a Match object? regexObject=re.compile(r'abc'), regexObject.findall.text(adeabc)
#5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)' , what does group 0 cover? Group 1 ? Group 2 ?group0=the whole numbers, group1= area code, group2=actual number
#6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters? \) \.
#7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other? by puting question mark
#What does the | character signify in regular expressions?it is for choose between two options

numRegex = re.compile(r'\d+') , what will numRegex.sub('X', '12 drummers, 11 pipers, five
rings, 3 hens')
