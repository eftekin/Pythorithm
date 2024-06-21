from tree_node import print_tree, sample_root_node

print_tree(sample_root_node)


def dfs(root, target, path=()):
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None


path = dfs(sample_root_node, "F")
print(path)
