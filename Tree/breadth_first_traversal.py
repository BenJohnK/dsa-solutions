from collections import deque


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


class Solution:
    def levelOrder(self, root):
        # code here
        result = []
        helper_deque = deque()
        helper_deque.append(root)
        while helper_deque:
            current_node = helper_deque.popleft()
            result.append(current_node.key)
            if current_node.left:
                helper_deque.append(current_node.left)
            if current_node.right:
                helper_deque.append(current_node.right)
        return result


obj = Solution()
print(obj.levelOrder(root))