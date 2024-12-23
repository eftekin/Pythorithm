"""Basic Node implementation for data structures."""

class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        """Return the value stored in the node."""
        return self.value

    def get_link_node(self):
        """Return the next node reference."""
        return self.link_node

    def set_link_node(self, link_node):
        """
        Set the next node reference.
        
        Args:
            link_node (Node): The node to link to
        """
        self.link_node = link_node


def demonstration():
    """Simple demonstration of node operations."""
    yacko = Node("likes to yak")
    wacko = Node("has a penchant for hoarding snacks")
    dot = Node("enjoys spending time in movie lots")

    # Link nodes
    dot.set_link_node(wacko)
    yacko.set_link_node(dot)

    # Access data through links
    dots_data = yacko.get_link_node().get_value()
    wackos_data = dot.get_link_node().get_value()

    # Display results
    print(f"Dot's data: {dots_data}")
    print(f"Wacko's data: {wackos_data}")


if __name__ == "__main__":
    demonstration()
