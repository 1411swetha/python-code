numbers = [10, 20, 77, 777, 30, 40]

div_by_7 = []
not_div_by_7 = []

for num in numbers:
    if num % 7 == 0:
        div_by_7.append(num)
    else:
        not_div_by_7.append(num)

print("Numbers divisible by 7:")
print(div_by_7)

print("\nNumbers NOT divisible by 7:")
print(not_div_by_7)

#Categorize student marks into Pass and Fail lists
# marks = [75, 32, 89, 45, 28, 90, 55, 38, 49, 60]

# passed_students = []
# failed_students = []

# for mark in marks:
#     if mark >= 40:
#         passed_students.append(mark)
#     else:
#         failed_students.append(mark)

# print("Passed students' marks:")
# print(passed_students)

# print("\nFailed students' marks:")
# print(failed_students)
