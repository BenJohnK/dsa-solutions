from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)





# 1 -> 2 -> null AND 4 -> 3 -> null

# 1 -> 4 -> 2 -> 3


# 10 -> 20 -> 30 AND 50 -> 40 -> null

# 10 -> 50 -> 20 -> 40 -> 30

class Solution:
    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
        
    def find_middle_ListNode(self, head):
        middle = head
        curr = head
        while curr.next and curr.next.next:
            middle = middle.next
            curr = curr.next.next
        return middle, middle.next
    
    def reverse_list(self, middle):
        prev = None
        curr = middle
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return

        prev_node, middle_ListNode = self.find_middle_ListNode(head)
        prev_node.next = None
        reversed_head = self.reverse_list(middle_ListNode)
        curr = head
        next_node = reversed_head

        # 10 -> 20 -> 30 AND 50 -> 40 -> null

        # 10 -> 50 -> 20 -> 40 -> 30

        while next_node:
            temp1 = curr.next
            temp2 = next_node.next

            curr.next = next_node
            next_node.next = temp1
            next_node = temp2
            curr = temp1

        self.print_list(head)

obj = Solution()
obj.reorderList(head)