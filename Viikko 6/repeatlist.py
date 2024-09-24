class RepeatList:
    def __init__(self):
        self.stack = set()
        self.multiple = False

    def add(self, x):
        if x not in self.stack:
            self.stack.add(x)
        else:
            self.multiple = True

    def check(self):
        return self.multiple

if __name__ == "__main__":
    r = RepeatList()
    print(r.check()) # False
    r.add(1)
    r.add(2)
    r.add(3)
    print(r.check()) # False
    r.add(2)
    print(r.check()) # True
    r.add(5)
    print(r.check()) # True