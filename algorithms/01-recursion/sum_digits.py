def sum_digits(n):
    if n <= 9:
        return n
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)


print(sum_digits(12345))  # prints 15
