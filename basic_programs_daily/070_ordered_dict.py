from collections import OrderedDict

ordered_dict = OrderedDict([("b", 2), ("c", 3), ("a", 4)])

# Item to insert at the beginning
new_item = ("d", 5)

# Create a new OrderedDict with the new item as the first element
new_ordered_dict = OrderedDict([new_item])

# Merge the new OrderedDict with the original OrderedDict
new_ordered_dict.update(ordered_dict)

# Print the updated OrderedDict
print("Updated OrderedDict:", new_ordered_dict)
