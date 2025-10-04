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

def insert_at_beginning(head, x):
    new_node = Node(x)
    new_node.next = head
    head = new_node
    return head


head = insert_at_beginning(head, 5)
print_linked_list(head)