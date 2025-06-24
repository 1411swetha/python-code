import re

text = "i,am,wonderfull,superb"

pattern = r","

res1 = re.split(pattern, text)
print(res1)