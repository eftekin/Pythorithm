# Write a Python program to print all pronic numbers between 1 and 100.

# A pronic number, also known as an oblong number or rectangular number, is a type of
# figurate number that represents a rectangle. It is the product of two consecutive integers, n
# and (n + 1).


def is_pronic_number(num):
    for n in range(1, int(num**0.5) + 1):
        if n * (n + 1) == num:
            return True


print("Pronic numbers between 1 and 100 are: ")
for i in range(1, 101):
    if is_pronic_number(i):
        print(i, end=" | ")
