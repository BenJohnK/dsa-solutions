class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(30)
head.next = Node(40)
head.next.next = Node(50)
head.next.next.next = Node(60)
head.next.next.next.next = head

def isCircular(head):
    # Code here
    curr = head
    while curr:
        if curr.next == head:
            return True
        if not curr.next:
            return False
        curr = curr.next

print(isCircular(head))

