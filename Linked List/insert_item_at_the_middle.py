class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def insert_at_middle(head: Node, x):
    if not head:
        new_node = Node(x)
        return new_node
    if not head.next:
        new_node = Node(x)
        head.next = new_node
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    new_node = Node(x)
    new_node.next = slow.next
    slow.next = new_node
    return head


head = insert_at_middle(head, 35)
print_linked_list(head)