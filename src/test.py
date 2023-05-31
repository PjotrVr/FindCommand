import re
from sys import exit

text = "My name is Peter and his name is Paul"
pattern = "is"
matches = re.finditer(pattern, text)
a = next(matches)
print(type(a))
print(a.start())
exit(0)
for match in matches:
    #print("Match found at start index:", match.start())
    #print("Match found at end index:", match.end())
    print(text[match.start():match.end() + 1])