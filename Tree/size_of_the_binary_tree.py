class ListNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root = ListNode(10)
root.left = ListNode(20)
root.left.left = ListNode(40)
root.left.right = ListNode(50)
root.left.right.left = ListNode(70)
root.left.right.right = ListNode(80)
root.right = ListNode(30)
root.right.right = ListNode(60)


def size_of_binary_tree(root):
    if not root:
        return 0
    size_of_left_binary_tree = size_of_binary_tree(root.left)
    size_of_right_binary_tree = size_of_binary_tree(root.right)
    return size_of_left_binary_tree + size_of_right_binary_tree + 1

print(size_of_binary_tree(root))