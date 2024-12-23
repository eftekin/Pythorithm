from node import Node


class Queue:
    """A Queue implementation using a linked list structure."""

    def __init__(self, max_size=None):
        """Initialize an empty queue with optional max_size."""
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        """Add an item to the end of the queue."""
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    def dequeue(self):
        """Remove and return the first item in the queue."""
        if self.get_size() > 0:
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")

    def peek(self):
        """Return the first item in the queue without removing it."""
        if self.is_empty():
            print("Nothing to see here!")
        else:
            return self.head.get_value()

    def get_size(self):
        """Return the number of items in the queue."""
        return self.size

    def has_space(self):
        """Check if there is space in the queue."""
        if self.max_size is None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0
