class Cities:
    def __init__(self, n):
        self.n = n
        self.graph = { node: [] for node in range( 1, n + 1 ) }

    def add_road(self, a, b):
        self.graph[ a ].append( b )
        self.graph[ b ].append( a )

    def has_route(self, a, b):
        self.visited = set()
        self.dfs( a )

        if b in self.visited:
            return True
        else:
            return False

    def dfs(self, x):
        if x in self.visited:
            return
        self.visited.add( x )

        for next_x in self.graph[ x ]:
            self.dfs( next_x )
        
if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1, 2)
    c.add_road(1, 3)
    c.add_road(4, 5)
    print(c.has_route(1, 5)) # False
    c.add_road(3, 4)
    print(c.has_route(1, 5)) # True