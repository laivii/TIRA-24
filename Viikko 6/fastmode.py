class FastMode:
    def __init__(self):
        self.stack = dict()
        self.the_mode = [ 0, 0 ]

    def add(self, x, k):
        if x not in self.stack:
            self.stack[ x ] = k
        else:
            self.stack[ x ] += k

        if self.the_mode[ 1 ] < self.stack[ x ]:
            self.the_mode[ 0 ] = x
            self.the_mode[ 1 ] = self.stack[ x ]
        elif self.the_mode[ 1 ] == self.stack[ x ] and self.the_mode[ 0 ] > x:
                self.the_mode[ 0 ] = x

    def mode(self):
        return self.the_mode[0]

if __name__ == "__main__":
    f = FastMode()
    f.add(10, 9)
    print(f.mode())
    f.add(6, 10)
    print(f.mode())
    f.add(10, 3)
    print(f.mode())
    f.add(6, 7)
    print(f.mode())
    f.add(6, 5)
    print(f.mode())
    f.add(7, 4)
    print(f.mode())
    f.add(6, 2)
    print(f.mode())
    f.add(7, 7)
    print(f.mode())
    f.add(2, 9)
    print(f.mode())
    f.add(6, 7)
    print(f.mode())