#! python3
# Find website URLs that begin with http:// or https://.
#import pyperclip, re
#urlRegex = re.compile(r'''([http://]|[https://])([a-zA-Z0-9._%+-])''', re.VERBOSE)
#text = str(pyperclip.paste())
#matches = []
#for groups in urlRegex.findall(text):
    #urlmatch='-'.join([groups[1], groups[2]])
    #matches.append(urlmatch)

#if len(matches) > 0:
  # pyperclip.copy('\n'.join(matches))
 #  print('Copied to clipboard:')
 #  print('\n'.join(matches))
#else:
#   print('No phone numbers or email addresses found.')

import pyperclip, re
#https://codereview.stackexchange.com/questions/223549/find-website-urls-that-begin-with-http-or-https
#protocol Regex - checks for http:// or https://
protocolRegex = re.compile(r'''
    https?://           #match http:// or https://
    (?:w{3}\.)?         #www-dot
       #domin name
                    #dot
    [a-zA-Z0-9._%+-./]+       #extension
    ''', re.VERBOSE)

text = str(pyperclip.paste()) #copying data from document to clipboard and converting it into a string
matches = [] #stores all matches in this list

for website in protocolRegex.findall(text): #finding website from the string text
    matches.append(website)

if len(matches) > 0:
    pyperclip.copy('\n'.join(map(str, matches))) #copying result to clipboard after adding newline after each match
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No website found')
