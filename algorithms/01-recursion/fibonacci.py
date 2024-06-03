def fibonacci(n):
    # base cases
    if n == 1:
        return n
    if n == 0:
        return n

    # recursive step
    print(f"Recursive call with {n} as input")
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
fibonacci_runtime = "2^N"
