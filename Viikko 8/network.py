class Network:
    def __init__(self, n):
        self.n = n
        self.graph = {node: [] for node in range( 1, n + 1 )}

    def add_link(self, a, b):
        self.graph[ a ].append( b )
        self.graph[ b ].append( a )

    def best_route(self, a, b):
        distances = {}

        queue = [ a ]
        distances[ a ] = 0

        for node in queue:
            distance = distances[ node ]
            for next_node in self.graph[ node ]:
                if next_node not in distances:
                    queue.append( next_node )
                    distances[ next_node ] = distance + 1

        if b in distances:
            return distances[ b ]
        else:
            return -1

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1, 2)
    w.add_link(2, 3)
    w.add_link(1, 3)
    w.add_link(4, 5)
    print(w.best_route(1, 5)) # -1
    w.add_link(3, 5)
    print(w.best_route(1, 5)) # 2