class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def reverse_linked_list(head1, head2):
    if not head2 or not head2.next:
        head2.next = head1
        return head2
    next = head2.next
    head2.next = head1
    new_head = reverse_linked_list(head2, next)
    return new_head

head = reverse_linked_list(None, head)
print_linked_list(head)