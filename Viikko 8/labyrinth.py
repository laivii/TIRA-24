class ShortestPaths:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, a, b):
        if a not in self.graph[ b ] and b not in self.graph[ a ]:
            self.graph[a].append(b)
            self.graph[b].append(a)

    def find_path(self, start_node, end_node):
        distances = {}
        previous = {}

        queue = [ start_node ]
        distances[ start_node ] = 0
        previous[ start_node ] = None

        for node in queue:
            distance = distances[ node ]
            for next_node in self.graph[ node ]:
                if next_node not in distances:
                    queue.append( next_node )
                    distances[ next_node ] = distance + 1
                    previous[ next_node ] = node

        if end_node not in distances:
            return -1

        node = end_node
        path = []
        while node:
            path.append( node )
            node = previous[ node ]

        path.reverse()

        return path.index( end_node )

def count(r):
    n = len( r )
    m = len( r[ 0 ])
    labyrinth = [ list( r[ x ]) for x in range( n )]

    nodes = []
    start_point = None
    end_point = None

    #  Find Nodes and start and end points
    for i in range( n ):
        for j in range( m ):
            node = labyrinth[ i ][ j ]

            if node != "#":
                nodes.append(( i, j ))

            if node == "A":
                start_point = ( i, j )

            if node == "B":
                end_point = ( i, j )

    s = ShortestPaths( nodes )

    #  Add edges
    neighbors = [( 1, 0 ), ( -1, 0 ), ( 0, 1 ), ( 0, -1 )]

    for node in nodes:
        for x, y in neighbors:
            neighbor = (node[ 0 ] + x, node[ 1 ] + y)
            if neighbor in nodes:  # Check if the neighbor is in the list of nodes
                s.add_edge( node, neighbor)

    #  Find shortest path 
    return s.find_path( start_point, end_point )

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7