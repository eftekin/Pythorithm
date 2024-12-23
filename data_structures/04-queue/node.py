class Node:
    """A Node class for linked data structures."""

    def __init__(self, value, next_node=None):
        """Initialize a Node with a value and optional next_node."""
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        """Set the next node reference."""
        self.next_node = next_node

    def get_next_node(self):
        """Get the next node reference."""
        return self.next_node

    def get_value(self):
        """Get the node's value."""
        return self.value
