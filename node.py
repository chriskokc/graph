# adjacency node
# Node {
#     graph_vertex* value
#     node* next
# }
# An adjacency node stores a graph vertex pointer as value

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
