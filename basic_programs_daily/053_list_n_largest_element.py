# Write a Python program to find N largest elements from a list.


def find_n_largest_elements(lst, n):
    sorted_lst = sorted(lst, reverse=True)

    largest_elements = sorted_lst[:n]

    return largest_elements


numbers = [30, 10, 45, 5, 3, 6, 7, 8, 100, 50, 55, 24, 90, 91, 67, 68]

N = int(input("N = "))
result = find_n_largest_elements(numbers, N)

print(f"The {N} largest elements in the list are:", result)
