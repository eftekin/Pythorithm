from build_bst import build_bst


def depth(tree):
    if not tree:
        return 0

    left_depth = depth(tree["left_child"])
    right_depth = depth(tree["right_child"])

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
