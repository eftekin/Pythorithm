# Write a Python program to Cloning or Copying a list.

original_list = [1, 2, 3, 4, 5]
cloned_list_1 = original_list[:]
print(cloned_list_1)

cloned_list_2 = list(original_list)
print(cloned_list_2)

cloned_list_3 = [item for item in original_list]
print(cloned_list_3)
