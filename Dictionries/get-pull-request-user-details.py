import requests
import json

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()
#print(complete_details)
for i in range(len(complete_details)):
    user_name = complete_details[i]["user"]["login"]
    print(user_name)
    no_pullRequest = complete_details[i]["number"]
    print(no_pullRequest)
    user_pulls = user_name + "/" + str(no_pullRequest)
    print(user_pulls)
