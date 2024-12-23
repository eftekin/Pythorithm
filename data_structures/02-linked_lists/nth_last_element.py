from linked_list import LinkedList

def nth_last_node(linked_list, n):
    """
    Find the nth last node in a linked list.
    
    Args:
        linked_list: LinkedList object
        n: Position from the end (1-based)
    
    Returns:
        Node: The nth last node or None if not found
    """
    if not linked_list or not linked_list.head_node or n < 1:
        return None

    current = None
    tail_seeker = linked_list.head_node
    count = 0
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current


def generate_test_linked_list():
    linked_list = LinkedList()
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list


test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 10)
print(nth_last.value)
