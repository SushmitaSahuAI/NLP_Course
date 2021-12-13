import re

regex = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
string = input('Enter a string: ')
match = re.findall(regex, string)
if match:
    print('Match found:', match)
else:
    print('Match not found.') 
