class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

head = Node(30)
head.next = Node(40)
head.next.prev = head
# head.next.next = Node(50)
# head.next.next.prev =head.next

def print_doubly_linked_list(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def delete_last_node(head):
    if not head or not head.next:
        return
    curr = head
    while curr.next:
        curr = curr.next
    curr.prev.next = None
    curr.prev = None
    return head

print_doubly_linked_list(head)

head = delete_last_node(head)

print_doubly_linked_list(head)