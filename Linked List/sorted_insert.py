class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = None

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


def sorted_insert(head: Node, x):
    if not head:
        head = Node(x)
        return head
    if head.data > x:
        new_node = Node(x)
        new_node.next = head
        return new_node
    curr = head
    while curr:
        if curr.data <= x and (curr.next == None or curr.next.data > x):
            new_node = Node(x)
            new_node.next = curr.next
            curr.next = new_node
            return head
        curr = curr.next

head = sorted_insert(head, 20)
head = sorted_insert(head, 100)
print_linked_list(head)