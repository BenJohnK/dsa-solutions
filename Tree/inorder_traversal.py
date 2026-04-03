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

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.key)
    inorder_traversal(root.right)

inorder_traversal(root)
