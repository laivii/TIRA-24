class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    if not node.children:
        return 1

    amount = 0

    for child in node.children:
        amount += count(child)

    return amount

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
           ])

    print(count(tree)) # 5