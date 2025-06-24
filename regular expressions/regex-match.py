import re

text = "i am wonderfull"

pattren = r"am"

match = re.match(pattren, text)

if match:
    print("Match found:", match.group())
else:
    print("mattching pattern not found")