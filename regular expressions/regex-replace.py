import re

text = "i am wonderfull"

pattern = r"wonderfull"

replace_key = "awesome"

res1 = re.sub(pattern, replace_key, text)
print(res1)