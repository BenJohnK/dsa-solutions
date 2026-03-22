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
head.next.next.next.next.next.next = Node(70)

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def reverse_linked(head1, head2):
    if not head2:
        return head1
    temp = head2.next
    head2.next = head1
    return reverse_linked(head2, temp)


head = reverse_linked(None, head)
print_linked_list(head)