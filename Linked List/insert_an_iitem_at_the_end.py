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

def insert_at_end(head, x):
    new_node = Node(x)
    if not head:
        head = new_node
        return head
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

head = insert_at_end(head, 10)
head = insert_at_end(head, 20)
print_linked_list(head)

