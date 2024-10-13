# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2
# elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a
# Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a
# Curzon number, or False otherwise.
# Examples

# is_curzon(5) ➞ True
# # 2 ** 5 + 1 = 33
# # 2 * 5 + 1 = 11
# # 33 is a multiple of 11
# is_curzon(10) ➞ False
# # 2 ** 10 + 1 = 1025
# # 2 * 10 + 1 = 21
# # 1025 is not a multiple of 21
# is_curzon(14) ➞ True
# # 2 ** 14 + 1 = 16385
# # 2 * 14 + 1 = 29
# # 16385 is a multiple of 29

# Curzon Number:
# It is defined based on a specific mathematical relationship involving powers of 2. An integer
# 'n' is considered a Curzon number if it satisfies the folowing condition:
# If (2^n + 1) is divisible by (2n + 1), then 'n' is a Curzon number.
# For example:
# If n = 5: 2^5 + 1 = 33, and 2*5 + 1 = 11. Since 33 is divisible by 11 (33 % 11 = 0), 5 is a
# Curzon number.
# Curzon number.
# If n = 10: 2^10 + 1 = 1025, and 2*10 + 1 = 21. 1025 is not divisible by 21, so 10 is not a
# Curzon numbers are a specific subset of integers with this unique mathematical property.


def is_curzon(num):
    numerator = 2**num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0


# Test cases
print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))
