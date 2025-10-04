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

def insert_item(head: Node | None, x, position):
    if not head and position == 1:
        new_node = Node(x)
        head = new_node
        return new_node
    if position == 1:
        new_node = Node(x)
        new_node.next = head
        head = new_node
        return head
    curr = head
    current_position = 1
    while curr:
        if current_position + 1 == position:
            new_node = Node(x)
            new_node.next = curr.next
            curr.next = new_node
            return head
        current_position += 1
        curr = curr.next
    return head

head = insert_item(head, 5, 1)
head = insert_item(head, 50, 6)

print_linked_list(head)