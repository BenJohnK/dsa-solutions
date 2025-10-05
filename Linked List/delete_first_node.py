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

def delete_first_node(head):
    if not head:
        return head
    head = head.next
    return head

head = delete_first_node(head)
head = delete_first_node(head)

print_linked_list(head)