from node import Node
# a wrapper of the linked list nodes


class AdjacencyList:
    def __init__(self):
        self.head = None

    def insert_front(self, x):
        new_node = Node(x)
        if self.head is not None:
            new_node.next = self.head
        # modify the head pointer
        self.head = new_node