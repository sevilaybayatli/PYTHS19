#! python3
import pyperclip, re
#Remove sensitive information such as Social Security or credit card numbers 03-14-2015, and 2015/3/14.
#1-800-772-1213
#

#rmRegex = re.compile(r'''[http|https://]?[\w{3}.]?[a-zA-Z./-]+''', re.VERBOSE)
dateRegex=re.compile(r'''(\s[\d{1}|\d{2}|\d{4}]+[/|-]+[\d{2}|\d{1}]+[-|/]+[\d{2}|\d{4}]+)''', re.VERBOSE)
rmRegex = re.compile(r'''(\s[a-zA-Z.]+)''', re.VERBOSE)
text = str(pyperclip.paste())

matches=[]
for date in dateRegex.findall(text):
       matches.append(date)
       matches.remove(date)
for url in rmRegex.findall(text):
       matches.append(url)
       

# Copy results to the clipboard.
if len(matches) > 0:
   pyperclip.copy(''.join(matches))
   print('Copied to clipboard:')
   print(''.join(matches))
else:
   print('No url addresses found.')
