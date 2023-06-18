class FindShortestPath:
    def __init__(self):
        print("Bellman-Ford")

    def load_data(self, filename):
        self.graph = []
        with open(filename, 'r') as file:
            for line in file:
                start, end, weight = map(int, line.strip().split(','))
                self.graph.append((start, end, weight))

    def initialize(self):
        self.vertices = set()
        for edge in self.graph:
            self.vertices.add(edge[0])
            self.vertices.add(edge[1])
        self.distances = {v: float('inf') for v in self.vertices}
        self.previous = {v: None for v in self.vertices}

    def find_path(self, r):
        self.distances[r] = 0
        num_vertices = len(self.vertices)
        for _ in range(num_vertices - 1):
            for start, end, weight in self.graph:
                if self.distances[start] + weight < self.distances[end]:
                    self.distances[end] = self.distances[start] + weight
                    self.previous[end] = start

    def print_path(self, r):
        print("print path")
        for vertex in sorted(self.vertices):
            path = []
            current_vertex = vertex
            while current_vertex is not None:
                path.insert(0, current_vertex)
                current_vertex = self.previous[current_vertex]
            if self.distances[vertex] == float('inf'):
                print(f"Vertex {vertex}: Unreachable")
            else:
                print(f"Vertex {vertex}: Shortest Distance = {self.distances[vertex]}, Shortest Path = {path}")