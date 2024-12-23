from linked_list import LinkedList


def find_middle(linked_list):
    """
    Find the middle node of a linked list using fast and slow pointers.
    
    Args:
        linked_list: LinkedList object
    
    Returns:
        Node: The middle node of the linked list
    """
    if not linked_list or not linked_list.head_node:
        return None
    
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow


def generate_test_linked_list(length):
    linked_list = LinkedList()
    for i in range(length, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list


test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
