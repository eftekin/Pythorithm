# Write a Python program to find largest number in a list.

numbers = [30, 10, -45, 5, 20]
minimum = numbers[0]

for i in numbers:
    if i > minimum:
        minimum = i

print("The largest number in the list is:", minimum)
