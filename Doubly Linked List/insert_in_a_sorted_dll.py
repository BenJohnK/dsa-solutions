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

def insert_in_sorted_dll(head, x):
    if not head:
        new_node = Node(x)
        return head
    if x < head.data:
        new_node = Node(x)
        new_node.next = head
        head.prev = new_node
        return new_node
    curr = head
    while curr.next and curr.next.data <= x:
        curr = curr.next
    new_node = Node(x)
    new_node.next = curr.next
    new_node.prev = curr
    curr.next = new_node
    if new_node.next:
        new_node.next.prev = new_node
    return head

print_doubly_linked_list(head)

head = insert_in_sorted_dll(head, 45)

print_doubly_linked_list(head)