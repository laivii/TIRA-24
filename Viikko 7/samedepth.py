class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check(node):
    depths = {}
    get_depths( node, 0 , depths )

    base_depth = 0

    for key in depths:
        depth = depths[ key ]
        
        if base_depth == 0:
            base_depth = depth

        if base_depth != depth:
            return False

    return True

def get_depths(node, depth, depths):
    if not node.children:
        depths[ node.value ] = depth

    for child in node.children:
        get_depths( child, depth + 1 , depths)

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3)]), Node(4, [Node(5), Node(6)])])

    print(check(tree1)) # False
    print(check(tree2)) # True