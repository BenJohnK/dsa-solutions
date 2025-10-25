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

def isCircular(head):
    #code here
    curr = head
    while curr.next != head and curr.next != None:
        curr = curr.next
    if curr.next == head:
        return True
    return False

print_doubly_linked_list(head)

print(isCircular(head))