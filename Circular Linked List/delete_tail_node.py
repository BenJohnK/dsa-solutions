class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(30)
head.next = Node(40)
head.next.next = Node(50)
head.next.next.next = Node(60)
head.next.next.next.next = head

def print_linked_list(head):
    if not head:
        return
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

def delete_tail(head):
    if not head:
        return
    curr = head
    while curr.next.next != head:
        curr = curr.next
    curr.next = head

delete_tail(head)

print_linked_list(head)