class Node:
    def __init__(self, value, next_node=None):
        """Initialize a node with a value and optional next node."""
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        """Initialize a linked list with an optional initial value."""
        self.head_node = Node(value) if value is not None else None

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        """Convert the linked list to a string representation."""
        if not self.head_node:
            return "Empty list"
        
        string_list = ""
        current = self.head_node
        while current:
            string_list += f"{current.get_value()} -> "
            current = current.get_next_node()
        return string_list + "None"

    def remove_node(self, value_to_remove):
        if not self.head_node:
            return
            
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
ll.remove_node(5)
print(ll.stringify_list())
