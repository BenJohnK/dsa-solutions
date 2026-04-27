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

def print_kth_nodes(root: ListNode, k):
    def find_and_print_nodes(root, depth):
        if not root:
            return
        if depth == k:
            print(root.key)
            return
        find_and_print_nodes(root.left, depth+1)
        find_and_print_nodes(root.right, depth+1)
    find_and_print_nodes(root, 0)

print_kth_nodes(root, 2)