def binary_search(sorted_list, left_pointer, right_pointer, target):
    if left_pointer >= right_pointer:
        return "value not found"

    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        return binary_search(sorted_list, left_pointer, mid_idx, target)
    if mid_val < target:
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))
