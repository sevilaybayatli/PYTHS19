import re

def checkOfString(string):
    chare=re.compile(r'[^a-zA-Z0-9.]')
    string=chare.search(string)
    return not bool(string)

print(checkOfString('AgfsrWCB12.'))
print(checkOfString('*"q@aQ'))


