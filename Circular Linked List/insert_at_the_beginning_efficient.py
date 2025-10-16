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

def insert_at_the_beginning(head: Node, x):
    if not head:
        new_node = Node(x)
        new_node.next = new_node
        return new_node
    new_node = Node(x)
    new_node.next = head.next
    head.next = new_node
    head.data, new_node.data = new_node.data, head.data
    return head

head = insert_at_the_beginning(head, 20)

print_linked_list(head)
