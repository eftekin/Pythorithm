# Create a function that takes a list of non-negative integers and strings and return a
# new list without the strings.

# Examples
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]
# filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
# filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]


def filter_list(lst):
    # Initialize an empty list to store non-string elements
    result = []

    # Iterate through the elements in the input list
    for element in lst:
        # Check if the element is a non-negative integer (not a string)
        if isinstance(element, int) and element >= 0:
            result.append(element)

    return result


print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))

