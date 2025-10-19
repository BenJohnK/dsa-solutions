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


def insertAtPosition(head,pos,data):
    #code here
    new_node = Node(data)
    curr = head
    if curr.next == head and pos > 1:
        return head
    for i in range(pos-1):
        curr = curr.next
        if curr == head:
            return head
    new_node.next = curr.next
    curr.next = new_node
    return head

head = insertAtPosition(head, 1, 35)
print_linked_list(head)