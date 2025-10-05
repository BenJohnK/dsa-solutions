class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def delete_last_node(head: Node):
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

head = delete_last_node(head)

print_linked_list(head)