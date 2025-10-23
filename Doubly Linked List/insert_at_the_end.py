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

def insert_at_the_end(head, x):
    new_node = Node(x)
    if not head:
        return new_node
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head

print_doubly_linked_list(head)

head = insert_at_the_end(head, 60)

print_doubly_linked_list(head)

head = insert_at_the_end(head, 70)

print_doubly_linked_list(head)

