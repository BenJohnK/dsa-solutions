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

def delete_head_node(head):
    if not head or not head.next:
        return None
    temp = head
    head = head.next
    head.prev = None
    temp.next = None
    return head

print_doubly_linked_list(head)

head = delete_head_node(head)

print_doubly_linked_list(head)