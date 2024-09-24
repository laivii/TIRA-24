class Mex:
    def __init__(self):
         self.stack = set()
         self.smallest = 0

    def add(self, x):
        if x not in self.stack:
            self.stack.add( x )

        the_smallest = self.find_mex()

        return the_smallest

    def find_mex( self ):
        while self.smallest in self.stack:
            self.smallest += 1

        return self.smallest

        

if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6