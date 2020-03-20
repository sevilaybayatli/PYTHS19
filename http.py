#! python3
import pyperclip, re
#Find website URLs that begin with http:// or https://.
#http//:takelessons.com/blog/best-singers-of-all-time-z02
urlRegex = re.compile(r'''[http|https://]?[\w{3}.]?[a-zA-Z./-]+''', re.VERBOSE)
text = str(pyperclip.paste())
matches=[]
for url in urlRegex.findall(text):
       matches.append(url)

# Copy results to the clipboard.
if len(matches) > 0:
   pyperclip.copy(''.join(matches))
   print('Copied to clipboard:')
   print(''.join(matches))
else:
   print('No url addresses found.')
