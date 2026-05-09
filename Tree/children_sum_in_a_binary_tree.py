'''
Given the root of a binary tree, determine whether the tree satisfies the Children Sum Property. In this property, each non-leaf node must have a 
value equal to the sum of its left and right children's values. A NULL child is considered to have a value of 0, and all leaf nodes are considered 
valid by default. Return true if every node in the tree satisfies this condition, otherwise return false.
'''

class ListNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root = ListNode(35)
root.left = ListNode(20)
root.left.left = ListNode(15)
root.left.right = ListNode(5)
root.right = ListNode(15)
root.right.left = ListNode(10)
root.right.right = ListNode(5)


def isSumProperty(root: ListNode):
    if not root.left and not root.right:
        return True
    left_child_value = root.left.key if root.left else 0
    right_child_value = root.right.key if root.right else 0
    if root.key != left_child_value + right_child_value:
        return False
    if root.left:
        is_left_ok = isSumProperty(root.left)
        if not is_left_ok:
            return False
    if root.right:
        is_right_ok = isSumProperty(root.right)
        if not is_right_ok:
            return False
    return True

print(isSumProperty(root))