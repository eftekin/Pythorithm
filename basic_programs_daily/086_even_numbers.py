# Please write a program using generator to print the even numbers between 0 and n in
# comma separated form while n is input by console.
# Example:
# If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10


def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num


try:
    n = int(input("Enter a value for n: "))
    result = even_numbers(n)
    print(",".join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")

    
