# Node class represents each element in the doubly linked list
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value  # Value of the node
        self.next_node = next_node  # Pointer to the next node
        self.prev_node = prev_node  # Pointer to the previous node

    def set_next_node(self, next_node):
        self.next_node = next_node  # Set the next node

    def get_next_node(self):
        return self.next_node  # Get the next node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node  # Set the previous node

    def get_prev_node(self):
        return self.prev_node  # Get the previous node

    def get_value(self):
        return self.value  # Get the value of the node


# DoublyLinkedList class represents the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head_node = None  # Head node of the list
        self.tail_node = None  # Tail node of the list

    def add_to_head(self, new_value):
        new_head = Node(new_value)  # Create a new node
        current_head = self.head_node  # Get the current head node

        if current_head is not None:
            current_head.set_prev_node(new_head)  # Set the new head as the previous node of the current head
            new_head.set_next_node(current_head)  # Set the current head as the next node of the new head

        self.head_node = new_head  # Update the head node

        if self.tail_node is None:
            self.tail_node = new_head  # If the list was empty, set the tail node to the new head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)  # Create a new node
        current_tail = self.tail_node  # Get the current tail node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)  # Set the new tail as the next node of the current tail
            new_tail.set_prev_node(current_tail)  # Set the current tail as the previous node of the new tail

        self.tail_node = new_tail  # Update the tail node

        if self.head_node is None:
            self.head_node = new_tail  # If the list was empty, set the head node to the new tail

    def remove_head(self):
        removed_head = self.head_node  # Get the current head node

        if removed_head is None:
            return None  # If the list is empty, return None

        self.head_node = removed_head.get_next_node()  # Update the head node to the next node

        if self.head_node is not None:
            self.head_node.set_prev_node(None)  # Set the previous node of the new head to None

        if removed_head == self.tail_node:
            self.remove_tail()  # If the removed head was the only node, update the tail node

        return removed_head.get_value()  # Return the value of the removed head

    def remove_tail(self):
        removed_tail = self.tail_node  # Get the current tail node

        if removed_tail is None:
            return None  # If the list is empty, return None

        self.tail_node = removed_tail.get_prev_node()  # Update the tail node to the previous node

        if self.tail_node is not None:
            self.tail_node.set_next_node(None)  # Set the next node of the new tail to None

        if removed_tail == self.head_node:
            self.remove_head()  # If the removed tail was the only node, update the head node

        return removed_tail.get_value()  # Return the value of the removed tail

    def remove_by_value(self, value_to_remove):
        if not self.head_node:
            return None  # If the list is empty, return None

        node_to_remove = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node  # Find the node to remove
                break

            current_node = current_node.get_next_node()

        if node_to_remove is None:
            return None  # If the value is not found, return None

        if node_to_remove == self.head_node:
            self.remove_head()  # If the node to remove is the head, remove the head
        elif node_to_remove == self.tail_node:
            self.remove_tail()  # If the node to remove is the tail, remove the tail
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)  # Update the previous node of the next node
            prev_node.set_next_node(next_node)  # Update the next node of the previous node
        
        return node_to_remove.get_value()  # Return the value of the removed node

    def stringify_list(self):
        if not self.head_node:
            return "Empty list"  # If the list is empty, return "Empty list"
            
        result = ""
        current = self.head_node
        while current:
            result += f"{current.get_value()} <-> "  # Append the value of each node to the result string
            current = current.get_next_node()
        return result + "None"  # Append "None" to indicate the end of the list


# Test code to verify the functionality of the doubly linked list
def test_doubly_linked_list():
    dll = DoublyLinkedList()
    dll.add_to_head("Times Square")
    dll.add_to_head("Grand Central")
    dll.add_to_head("Central Park")

    print(dll.stringify_list())  # Expected: Central Park <-> Grand Central <-> Times Square <-> None

    dll.add_to_tail("Penn Station")
    dll.add_to_tail("Wall Street")
    dll.add_to_tail("Brooklyn Bridge")

    print(dll.stringify_list())  # Expected: Central Park <-> Grand Central <-> Times Square <-> Penn Station <-> Wall Street <-> Brooklyn Bridge <-> None

    dll.remove_head()
    dll.remove_tail()
    print(dll.stringify_list())  # Expected: Grand Central <-> Times Square <-> Penn Station <-> Wall Street <-> None

    dll.remove_by_value("Times Square")
    print(dll.stringify_list())  # Expected: Grand Central <-> Penn Station <-> Wall Street <-> None

test_doubly_linked_list()
