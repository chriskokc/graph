# Undirected graph implementation using adjacency list
# hash map
# graph = {
#     string: graph_vertex pointer,
# }
# graph = {
# ...     1: [2, 3, None],
# ...     2: [4, None],
# ...     3: [None],
# ...     4: [5, 6, None],
# ...     5: [6, None],
# ...     6: [None]
# ... }

from adjacency_list import AdjacencyList
from graph_vertex import GraphVertex
from queue import Queue


class Graph:
    def __init__(self, V):
        self.graph = {}
        # each item is the list keeping track of the adjacency list for each graph vertex
        self.V = [None for i in range(V)]
        # for DFS
        self.status = [False for i in range(V)]

    def add_edges(self, source, destination):
        # for source graph vertex
        # create a graph vertex
        destination_graph_vertex = GraphVertex(destination)
        # create an adjacency node
        # insert the node to a linked list, i.e adjacency list
        source_adjacency_list = AdjacencyList()
        if self.V[source] is not None:
            source_adjacency_list = self.V[source]
        source_adjacency_list.insert_front(destination_graph_vertex)
        # update the adjacency list stored for each graph vertex
        self.V[source] = source_adjacency_list
        # append the list of references to the source graph vertex
        source_graph_vertex = GraphVertex(source)
        source_graph_vertex.edges.append(source_adjacency_list)
        # map the key (name) with the value (graph vertex pointer)
        self.graph[source_graph_vertex.vertex] = source_graph_vertex
        # repeat the above for destination graph vertex as it is an undirected graph
        destination_adjacency_list = AdjacencyList()
        if self.V[destination] is not None:
            destination_adjacency_list = self.V[destination]
        destination_adjacency_list.insert_front(source_graph_vertex)
        # update the adjacency list stored for each graph vertex
        self.V[destination] = destination_adjacency_list
        destination_graph_vertex.edges.append(destination_adjacency_list)
        self.graph[destination_graph_vertex.vertex] = destination_graph_vertex

    def print_graph(self):
        for (vertex, graph_vertex_pointer) in sorted(self.graph.items()):
            print(f"Adjacency list of vertex {vertex}\n head", end="")
            adjacency_graph_vertices = graph_vertex_pointer.edges[0]
            while adjacency_graph_vertices.head is not None:
                print(f"-> {adjacency_graph_vertices.head.value.vertex}", end="")
                adjacency_graph_vertices.head = adjacency_graph_vertices.head.next
            print("\n")

    def breadth_first_search(self, source):
        """we explore the starting vertex,
        discovering its surrounding vertices for exploration afterwards."""
        # create a new queue
        exploration_queue = Queue()
        # enqueue the source node
        exploration_queue.enqueue(source.vertex)
        # create a hash map for tracking status for vertices
        status_map = {}
        # mark the source node as discovered
        status_map[source.vertex] = "marked"
        # while the queue is not empty
        while not exploration_queue.is_empty():
            # dequeue the node and explore it
            explored_vertex = exploration_queue.dequeue()
            print(f"The explored vertex is {explored_vertex}.")
            # discover its surrounding nodes
            adjacency_graph_vertices = self.graph[explored_vertex].edges[0]
            while adjacency_graph_vertices.head is not None:
                discovered_vertex = adjacency_graph_vertices.head.value.vertex
                # if it is unmarked, enqueue those surrounding nodes to the queue
                if discovered_vertex not in status_map:
                    # mark them
                    status_map[discovered_vertex] = "marked"
                    exploration_queue.enqueue(discovered_vertex)
                adjacency_graph_vertices.head = adjacency_graph_vertices.head.next

    def depth_first_search(self, source):
        """we discover nodes and go as deep as possible.
        Once we finish a node, we retrace and discover other nodes again."""
        # mark the current vertex as discovered
        self.status[source.vertex] = True
        print(f"The discovered vertex is {source.vertex}.")
        # for other vertices of current vertex
        adjacency_graph_vertices = self.graph[source.vertex].edges[0]
        while adjacency_graph_vertices.head is not None:
            # if its status is undiscovered, we discover it
            if not self.status[adjacency_graph_vertices.head.value.vertex]:
                # apply recursion
                self.depth_first_search(adjacency_graph_vertices.head.value)
            # assign the head to next vertex
            adjacency_graph_vertices.head = adjacency_graph_vertices.head.next
        # if there is no more discovered vertices for the current vertex, we finish it
        print(f"The finished vertex is {source.vertex}.")