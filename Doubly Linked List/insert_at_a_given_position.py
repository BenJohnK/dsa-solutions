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

def insert_at_pos(head, p, x):
        # Code Here
        if not head.next and p > 0:
            return head
        curr = head
        for i in range(p):
            if not curr:
                return head
            curr = curr.next
        new_node = Node(x)
        if not curr.next:
            curr.next = new_node
            new_node.prev = curr
        else:
            new_node.next = curr.next
            curr.next = new_node
            new_node.next.prev = new_node
            new_node.prev = curr
        return head

print_doubly_linked_list(head)

insert_at_pos(head, 1, 45)

print_doubly_linked_list(head)