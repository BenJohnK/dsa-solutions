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

def reverse_linked_list(head):
    if not head or not head.next:
        return head
    curr = head.next
    while curr:
        temp = curr.next
        curr.next = head
        head = head.next
        curr = temp
    return head

head = reverse_linked_list(head)
print(head.data)
# print_linked_list(head)