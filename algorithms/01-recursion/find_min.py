def find_min(my_list, min=None):
    if not my_list:
        return min

    if not min or my_list[0] < min:
        min = my_list[0]
    return find_min(my_list[1:], min)


print(find_min([42, 17, 2, -1, 67]))
