from node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the stack!".format(value))
        else:
            print("There is no space for {}.".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This stack is totally empty.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0


pizza_stack = Stack(6)

pizza_stack.push("Pizza #1")
pizza_stack.push("Pizza #2")
pizza_stack.push("Pizza #3")
pizza_stack.push("Pizza #4")
pizza_stack.push("Pizza #5")
pizza_stack.push("Pizza #6")
pizza_stack.push("Pizza #7")  # overflow


print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

pizza_stack.peek()
