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

