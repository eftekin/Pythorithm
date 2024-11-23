# Create a function that reverses a boolean value and returns the string "boolean
# expected" if another variable type is given.
# Examples
# reverse(True) ➞ False
# reverse(False) ➞ True
# reverse(0) ➞ "boolean expected"
# reverse(None) ➞ "boolean expected"


def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"


print(reverse(True))
print(reverse(False))
print(reverse(0))
print(reverse(None))
