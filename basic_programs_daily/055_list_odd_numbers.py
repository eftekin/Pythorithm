# Write a Python program to print odd numbers in a List.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers in the list:", odd_numbers)
