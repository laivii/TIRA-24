class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    depths = []
    count_helper( node, 0, depths )

    result = 0

    for depth in depths:
        result += depth
        
    return result

def count_helper(node, depth, depths):
    depths.append( depth )

    for child in node.children:
        count_helper(child, depth + 1, depths)


if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 15