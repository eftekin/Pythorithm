# Write a Python program to find second largest number in a list.

numbers = [30, 10, 45, 5, 20]

numbers.sort(reverse=True)

if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")
