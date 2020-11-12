# Regular Expressions - Regex

text = "The agent's phone number is 408-555-1234. Call soon"

print("phone" in text)

import re

pattern = "phone"

#TAKES PATTERN, AND SCANS THE TEXT TO SEARCH
print(re.search(pattern,text)) # output: <re.Match object; span=(12, 17), match='phone'>
match = re.search(pattern,text)
print(match.span()) # (12,17)
print(match.start()) # 12
print(match.end()) # 17

text = "my phone once, my phone twice"
matches = (re.findall("phone",text))
print(matches) # number of times the text "phone" shows up
print(len(matches))


for match in re.finditer("phone",text):
    print(match.group())
