import re

text = "i am wonderfull"

pattern = r"am"

res1 = re.search(pattern, text)

if res1:
    print("Pattern found:", res1.group())
else:
    print("Pattern not found")