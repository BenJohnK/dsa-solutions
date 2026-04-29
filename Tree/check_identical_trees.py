class ListNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root1 = ListNode(10)
root1.left = ListNode(20)
root1.left.left = ListNode(40)
root1.left.right = ListNode(50)
root1.left.right.left = ListNode(70)
root1.left.right.right = ListNode(80)
root1.right = ListNode(30)
root1.right.right = ListNode(60)

root2 = ListNode(10)
root2.left = ListNode(20)
root2.left.left = ListNode(40)
root2.left.right = ListNode(50)
root2.left.right.left = ListNode(70)
root2.left.right.right = ListNode(80)
root2.right = ListNode(30)
root2.right.right = ListNode(60)

def is_identical_trees(root1: ListNode, root2: ListNode) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.key != root2.key:
        return False
    return is_identical_trees(root1.left, root1.left) and is_identical_trees(root1.right, root2.right)


print(is_identical_trees(root1, root2))
