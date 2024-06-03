def sum_to_one(n):
    if n == 1:
        return n
    else:
        return n + sum_to_one(n - 1)
        print(f"Recursing with input: {n}")


print(sum_to_one(7))
