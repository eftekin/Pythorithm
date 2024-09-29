# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence in
# comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 8
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13


def fibonacci(n):
    sequence = [0, 1]  # Initializing the sequence with the first two element
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
    return sequence


try:
    n = int(input("Enter a value for n: "))
    result = fibonacci(n)
    print(",".join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
