class QuickList:
    def __init__(self, t):
        self.index = 0
        self.stack = t
        self.length = len( t )

    def move(self, k):
        self.index += k

        if self.index >= self.length:
            self.index = self.index % self.length

    def get(self, i):
        k = self.index + i
        
        if k >= self.length:
            k = k % self.length

        return self.stack[ k ]

if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9