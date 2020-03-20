#! python3
import pyperclip, re

#Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by replacing them with dates in a single, standard format.

dateRegex=re.compile(r'''(\s[\d{1}|\d{2}|\d{4}]+[/|-]+[\d{2}|\d{1}]+[-|/]+[\d{2}|\d{4}]+)''', re.VERBOSE)

text = str(pyperclip.paste())
matches=[]
for date in dateRegex.findall(text):
       nu = re.compile(r'[-|/]')
       
       matches.append(nu.sub('-', date))

# Copy results to the clipboard.
if len(matches) > 0:
   pyperclip.copy(''.join(matches))
   print('Copied to clipboard:')
   print(''.join(matches))
else:
   print('No date addresses found.')
