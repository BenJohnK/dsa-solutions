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


def maximum_in_binary_tree(root: ListNode):
    if not root:
        return -float('inf')
    left_max_value = maximum_in_binary_tree(root.left)
    right_max_value = maximum_in_binary_tree(root.right)
    return max(root.key, left_max_value, right_max_value)

print(maximum_in_binary_tree(root))