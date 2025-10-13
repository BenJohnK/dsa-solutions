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
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

print_linked_list(head)