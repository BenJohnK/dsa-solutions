class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

def search(head, x):
    curr = head
    current_position = 1
    while curr != None:
        if curr.data == x:
            return current_position
        current_position += 1
        curr = curr.next
    return -1

print(search(head, 0))