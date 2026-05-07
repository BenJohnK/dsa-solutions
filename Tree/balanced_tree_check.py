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


def balanced_tree_check(root: ListNode):
    if not root:
        return 0, True
    left_height, is_left_balanced = balanced_tree_check(root.left)
    if not is_left_balanced:
        return left_height + 1, False
    right_height, is_right_balanced = balanced_tree_check(root.right)
    if not is_right_balanced:
        return right_height + 1, False
    if not abs(left_height-right_height) <= 1:
        return max(left_height, right_height) + 1, False
    return max(left_height, right_height) + 1, True


print(balanced_tree_check(root)[1])