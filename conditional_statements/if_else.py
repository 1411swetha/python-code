import sys

key = sys.argv[1]

if key == "t2.micro":
    print("creating.it will cost 2$/day")
elif key == "t2.medium":
    print("creating.it will cost 4$/day")
elif key == "t2.large":
    print("creating.it will cost 2$/day")
else:
    print("wrong instance type")