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
    if not head:
        return
    print(head.data)
    curr = head.next
    while curr != head:
        print(curr.data)
        curr = curr.next

def delete_head_node(head):
    if not head or head.next == head:
        return None
    head.data = head.next.data
    head.next = head.next.next
    return head

head = delete_head_node(head)

print_linked_list(head)
