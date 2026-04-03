class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None

#driver code

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

