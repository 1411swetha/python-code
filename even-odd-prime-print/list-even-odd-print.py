even_numbers = []
odd_numbers = []
numbers = [1, 2, 3, 4, 5]

print("printing even nos:")
for i in numbers:
    if i % 2 ==  0:
        print(i)
        even_numbers.append(i)
print("printing odd nos:")
for i in numbers:
    if i % 2 !=  0:
        print(i)
        odd_numbers.append(i)

