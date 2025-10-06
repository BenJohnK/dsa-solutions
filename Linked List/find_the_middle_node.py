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

def find_middle_node(head):
    if not head:
        return None
    if not head.next:
        return head.data
    middle = head.next
    curr = head.next.next
    pos = 1
    while curr:
        if pos & 1 == 0:
            middle = middle.next
        pos = pos + 1
        curr = curr.next
    return middle.data

print(find_middle_node(head))