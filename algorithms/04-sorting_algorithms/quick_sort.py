from random import randrange, shuffle


# Function to perform quicksort on a list
def quicksort(list, start, end):
    # Base case: if the starting index is greater than or equal to the ending index, return
    if start >= end:
        return

    # Select a random pivot index between start and end (inclusive)
    pivot_idx = randrange(start, end + 1)
    # Get the pivot element from the list
    pivot_element = list[pivot_idx]

    # Swap the pivot element with the element at the end
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # Initialize the less_than_pointer to the start
    less_than_pointer = start

    # Partition the list around the pivot element
    for i in range(start, end):
        # If the current element is less than the pivot element
        if list[i] < pivot_element:
            # Swap the current element with the element at the less_than_pointer
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # Move the less_than_pointer to the right
            less_than_pointer += 1

    # Swap the pivot element back to its correct position
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

    # Recursively apply quicksort to the left partition
    quicksort(list, start, less_than_pointer - 1)
    # Recursively apply quicksort to the right partition
    quicksort(list, less_than_pointer + 1, end)


# Create an unsorted list
unsorted_list = [3, 7, 12, 24, 36, 42]

# Shuffle the list to randomize the order
shuffle(unsorted_list)
print(unsorted_list)  # Print the unsorted list

# Perform quicksort on the unsorted list
quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)  # Print the sorted list
