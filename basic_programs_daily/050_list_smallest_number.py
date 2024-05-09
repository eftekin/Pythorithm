# Write a Python program to find smallest number in a list.

numbers = [30, 10, 100, 5, 20, -1]
minimum = numbers[0]

for i in numbers:
    if i < minimum:
        minimum = i


print("The smallst number in the list is:", minimum)
