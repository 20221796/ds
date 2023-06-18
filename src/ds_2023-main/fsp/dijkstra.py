class FindShortestPath:
    def __init__(self):
        print("Dijkstra")

    def load_data(self, filename):
        self.graph = {}
        with open(filename, 'r') as file:
            for line in file:
                start, end, weight = map(int, line.strip().split(','))
                if start not in self.graph:
                    self.graph[start] = {}
                self.graph[start][end] = weight

    def initialize(self):
        self.distances = {v: float('inf') for v in self.graph}
        self.previous = {v: None for v in self.graph}

    def find_path(self, r):
        visited = set()
        self.distances[r] = 0

        while len(visited) < len(self.graph):
            min_distance = float('inf')
            current_vertex = None

            for vertex in self.graph:
                if vertex not in visited and self.distances[vertex] < min_distance:
                    min_distance = self.distances[vertex]
                    current_vertex = vertex

            visited.add(current_vertex)

            for neighbor, weight in self.graph[current_vertex].items():
                distance = self.distances[current_vertex] + weight
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.previous[neighbor] = current_vertex

    def print_path(self, r):
        print("print path")
        for vertex in sorted(self.graph.keys()):
            path = []
            current_vertex = vertex
            while current_vertex is not None:
                path.insert(0, current_vertex)
                current_vertex = self.previous[current_vertex]
            if self.distances[vertex] == float('inf'):
                print(f"Vertex {vertex}: Unreachable")
            else:
                print(f"Vertex {vertex}: Shortest Distance = {self.distances[vertex]}, Shortest Path = {path}")