class MaxList:
    def __init__(self):
        self.stack = []
        self.max_num = [0]

    def add(self, x):
        if x > self.max_num[0]:
            self.max_num[0] = x

        self.stack.append( x )

    def max(self):
        if self.max_num[0] == 0:
            return None
        else:
            return self.max_num[0]

if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8