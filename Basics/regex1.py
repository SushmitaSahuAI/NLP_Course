import re
regex = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
string = input('Enter a string: ')
match = re.search(regex, string)
if match:
    print('Match found:', match.group())
else:
    print('Match not found.')
