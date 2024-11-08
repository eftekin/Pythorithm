# Write a function that calculates the factorial of a number recursively.


def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Revursive case: n! = n * (n-1)


# test cases
print(factorial(1))
print(factorial(10))
print(factorial(4))
print(factorial(0))
