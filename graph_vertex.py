# graph_vertex {
#     string name
#     AdjacencyList* edge
# }
# A graph vertex contains two things:
# 1. a name, and
# 2. a list of references to other graph vertices

class GraphVertex:
    def __init__(self, name):
        self.vertex = name
        self.edges = []