# Write a Python program to Count occurrences of an element in a list.


def count_occurences(list, element):
    count = list.count(element)
    return count


# usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6]
element_to_count = 2

occurences = count_occurences(my_list, element_to_count)
print(f'The element "{element_to_count}" appears {occurences} times in the list.')
