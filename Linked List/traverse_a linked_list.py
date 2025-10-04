def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

printLinkedList(head)

