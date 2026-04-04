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

def preorder_traversal(root):
    if not root:
        return
    print(root.key)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

preorder_traversal(root)