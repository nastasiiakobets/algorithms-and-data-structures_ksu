class OrientedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, start, end):
        self.adjacency_matrix[start][end] = 1

# Приклад використання
graph = OrientedGraph(4)
graph.add_edge(0, 1)
graph.add_edge(1, 2)

# Виведення матриці суміжності на екран
for row in graph.adjacency_matrix:
    print(row)