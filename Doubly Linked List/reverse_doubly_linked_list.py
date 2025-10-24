class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

head = Node(30)
head.next = Node(40)
head.next.prev = head
head.next.next = Node(50)
head.next.next.prev =head.next

def print_doubly_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def reverse_doubly_linked_list(head):
    if not head:
        return
    if not head.next:
        return head
    curr = head
    while curr:
        temp = curr.next
        curr.next, curr.prev = curr.prev, curr.next
        if temp:
            curr = temp
        else:
            break
    return curr

print_doubly_linked_list(head)

head = reverse_doubly_linked_list(head)

print_doubly_linked_list(head)