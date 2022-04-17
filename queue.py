# queue ADT
# interface: enqueue, dequeue, check if it is empty, peek
# implementation: linked list
# struct queue {
#     node* front;
#     node* back;
# }

from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def is_empty(self):
        # if a queue is empty, its front and back pointers will point to null
        return self.length == 0

    def peek(self):
        # return the value without dequeue
        # if the queue is empty
        if self.is_empty():
            print("The queue is empty.")
        # if the queue is not empty
        else:
            return self.front.value

    def enqueue(self, value):
        # create a new node for the input value
        new_node = Node(value)
        # if the queue is empty
        if self.is_empty():
            self.front = new_node
        else:
            # add the new node to the back of the queue
            # create a connection to the last node
            self.back.next = new_node
        # modify the back pointer
        self.back = new_node
        self.length += 1

    def dequeue(self):
        # if the queue is empty
        if self.is_empty():
            print("The queue is empty.")
        else:
            # remove the front
            value = self.front.value
            # disconnect the node and modify the front pointer
            self.front = self.front.next
            self.length -= 1
            # return the value
            return value

