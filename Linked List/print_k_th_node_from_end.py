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

def print_k_th_node_from_end(head, k):
    if not head:
        print("-1")
    pos = 1
    target = None
    curr = head
    while curr:
        if target:
            target = target.next
        elif pos == k:
            target = head
        pos += 1
        curr = curr.next
    if target:
        print(target.data)
    else:
        print("-1")

print_k_th_node_from_end(head, 3)