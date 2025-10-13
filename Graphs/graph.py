class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
            return True
        return False
   
    def remove_edge(self, v1, v2):
        if v1 in self.adjacency_list.keys() and v2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[v1].remove(v2)
                self.adjacency_list[v2].remove(v1)
                return True
            except ValueError:
                pass
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for next_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[next_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    def print_vertex(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")
        return True

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_edge("B", "A")
my_graph.add_edge("C", "A")
my_graph.add_edge("D", "A")
my_graph.add_edge("D", "B")
my_graph.remove_vertex("D")

# my_graph.remove_edge("A", "B")
my_graph.print_vertex()