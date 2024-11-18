# Write a function that moves all elements of one type to the end of the list.
# Examples
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
# move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
# move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]


def move_to_end(lst, element):
    # initialize a count for the specified element
    count = lst.count(element)

    # remove all occurrences of the element from the list
    lst = [x for x in lst if x != element]

    # append the element to the end of the list count times
    lst.extend([element] * count)

    return lst


# test cases
print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))
