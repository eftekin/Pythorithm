# Write a Python program to convert key-values list to flat dictionary.

key_values_list = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
# Initialize an empty dictionary
flat_dict = {}
# Iterate through the list and add key-value pairs to the dictionary
for key, value in key_values_list:
    flat_dict[key] = value

print("Flat Dictionary:", flat_dict)
