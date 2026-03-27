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
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = ListNode(60)


class Solution:
    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


obj = Solution()
head = obj.removeNthFromEnd(head, 5)
obj.print_linked_list(head)
