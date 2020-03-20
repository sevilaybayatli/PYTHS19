#Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14	) by replacing them with dates in a single, standard format.

import pyperclip, re
dateRegex=re.compile(r'''[0-9]+[-|/][0-9]+[-|/][0-9\s]+''', re.VERBOSE)
dateRegex.sub(r'[0-9]+[-][0-9]+[-][0-9\s]+','[0-9]+[-|/][0-9]+[-|/][0-9\s]+')


text = str(pyperclip.paste()) 
matches = [] 

for date in dateRegex.findall(text):
    #newregex=re.compile(r'''[0-9]+[-|/][0-9]+[-|/][0-9\s]+''', re.VERBOSE)
    
    matches.append(dateRegex)
#if len(matches) > 0:
 #   pyperclip.copy(''.join(map(str, matches)))
 #   print('Copied to clipboard:')
 #   print(' '.join(matches))
#else:
  #  print('No date found')
