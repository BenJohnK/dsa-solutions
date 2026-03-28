from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)


head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)



# 9 0 9
# 9 0 9

# 8 1 8 1

class Solution:
    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_start_dummy_node = ListNode(-1)
        tail = result_start_dummy_node
        head = result_start_dummy_node
        remainder_value = 0
        while l1 or l2:
            if not l2:
                new_node_val = (l1.val + remainder_value) % 10
                remainder_value = (l1.val + remainder_value)//10
                new_node = ListNode(new_node_val)
                tail.next = new_node
                tail = tail.next
                l1 = l1.next
            elif not l1:
                new_node_val = (l2.val + remainder_value) % 10
                remainder_value = (l2.val + remainder_value)//10
                new_node = ListNode(new_node_val)
                tail.next = new_node
                tail = tail.next
                l2 = l2.next
            else:
                new_node_val = (l1.val + l2.val + remainder_value) % 10
                remainder_value = (l1.val + l2.val + remainder_value)//10
                new_node = ListNode(new_node_val)
                tail.next = new_node
                tail = tail.next
                l1 = l1.next
                l2 = l2.next
        if remainder_value:
            new_node = ListNode(1)
            tail.next = new_node
            tail = tail.next
        return head.next

obj = Solution()
new_head = obj.addTwoNumbers(head1, head2)
obj.print_linked_list(new_head)