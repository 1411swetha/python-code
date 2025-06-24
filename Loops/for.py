##simple for loop executes on range
for i in range(10):
    print(i)

##for loop executes on list
colours = ["yellow", "red", "black"]

for x in colours:
    print(x)
##for loop executes on tuple
colour = ("yellow", "red", "black", "white")

for y in colour:
    print(y)
print(len(colour))

##read the file content and run the loop for each value in file
with open("1.txt", "r") as file:
    for t in file:
        print(t)
