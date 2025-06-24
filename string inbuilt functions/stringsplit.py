arn = "arn:aws:iam::123456789012:user/johndoe"

user = arn.split("/")[1]

print("user name is:", user)

# user = arn.split(":")[5]
# username = user.split("/")[1]
# print(username)
