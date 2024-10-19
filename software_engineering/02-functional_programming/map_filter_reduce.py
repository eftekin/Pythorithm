from functools import reduce

# Example 1: Filtering and mapping
nums = (16, 2, 19, 22, 10, 23)

# Filter even numbers and then map to their double
even_numbers = filter(lambda x: x % 2 == 0, nums)
doubled_evens = map(lambda x: x * 2, even_numbers)

print(tuple(doubled_evens))  # Output: (32, 4, 44, 20)

# Example 2: Using reduce to sum the numbers
total_sum = reduce(lambda x, y: x + y, nums)
print(total_sum)  # Output: 92

# Example 3: More complex filtering and mapping
greater_than_10_doubled = map(lambda x: x * 2, filter(lambda y: y > 10, nums))
print(tuple(greater_than_10_doubled))  # Output: (32, 38, 44, 46)
