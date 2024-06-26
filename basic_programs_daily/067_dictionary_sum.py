# Write a Python program to find the sum of all items in a dictionary.
my_dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}

total_sum = 0

for i in my_dict.values():
    total_sum += i

print("Sum of all items in the dictionary:", total_sum)
