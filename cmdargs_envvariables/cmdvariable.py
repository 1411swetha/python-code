import sys

def add(num1, num2):
    add = num1 + num2
    return add
def sub(num1, num2):
    sub = num1 - num2
    return sub
def mul(num1, num2):
    mul = num1 * num2
    return mul
##manual values
# print(add(10, 5))
# print(sub(10, 5))
# print(mul(10, 5))

##defining arguments from cmd line 
num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == "add":
    res1 = num1 + num2
    print(res1)
elif operator == "sub":
    res2 = num1 - num2
    print(res2)
elif operator == "mul":
    res3 = num1 * num2
    print(res3)
else: 
    print("function not defined")

