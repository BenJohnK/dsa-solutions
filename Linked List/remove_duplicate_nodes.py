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

def remove_duplicate_nodes(head):
    if not head or not head.next:
        return
    end = head
    curr = head.next
    while curr:
        if curr.data != end.data:
            end.next = curr
            end = curr
        curr = curr.next
    end.next = None


remove_duplicate_nodes(head)
print_linked_list(head)