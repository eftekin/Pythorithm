# Higher-order function that takes functions as arguments
def odd_or_even(n, even_func, odd_func):
    """Calls the appropriate function based on whether n is odd or even."""
    if n % 2 == 0:
        return even_func(n)
    else:
        return odd_func(n)


# Lambda expressions for square and cube
square = lambda x: x * x
cube = lambda x: x * x * x

# Test the higher-order function
result = odd_or_even(5, square, cube)
print(result)  # Output: 125
