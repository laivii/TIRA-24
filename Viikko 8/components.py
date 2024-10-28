class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def visit(self, node):
        if node in self.components:
            return
        self.components[node] = self.counter

        for next_node in self.graph[node]:
            self.visit(next_node)

    def find_components(self):
        self.counter = 0
        self.components = {}

        for node in self.nodes:
            if node not in self.components:
                self.counter += 1
                self.visit(node)

        return self.counter

nodes =  []
N = 1000 


for i in range(2, N + 2):
    nodes.append(i)

c = Components(nodes)

for a in nodes:
    for b in nodes:
        if a % b == 0 or b % a == 0 and a != b:
            c.add_edge(a, b)

print(c.find_components())