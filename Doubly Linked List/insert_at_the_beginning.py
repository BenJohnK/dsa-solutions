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

def insert_at_the_beginning(head, x):
    new_node = Node(x)
    if not head:
        return new_node
    new_node.next = head
    head.prev = new_node
    return new_node

print_doubly_linked_list(head)
head = insert_at_the_beginning(head, 20)
print_doubly_linked_list(head)
