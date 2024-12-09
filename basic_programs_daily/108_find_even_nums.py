# Using list comprehensions, create a function that finds all even numbers from 1 to
# the given number.
# Examples
# find_even_nums(8) ➞ [2, 4, 6, 8]
# find_even_nums(4) ➞ [2, 4]
# find_even_nums(2) ➞ [2]


def find_even_nums(num):
    # Use a list comprehension to generate even numbers from 1 to num
    return [x for x in range(1, num + 1) if x % 2 == 0]


# test cases
print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))
