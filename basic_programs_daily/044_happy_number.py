# Write a Python program to check if the given number is Happy Number.

# Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
# the number by the sum of the squares of its digits and continue the process, eventualy
# reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
# is not a Happy Number.


def is_happy_number(num):
    seen = set()  # to store previously seen numbers

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))

    return num == 1


num = int(input("Enter a number: "))
if is_happy_number(num):
    print(str(num) + " is a Happy Number")
else:
    print(str(num) + " is not a Happy Number")
