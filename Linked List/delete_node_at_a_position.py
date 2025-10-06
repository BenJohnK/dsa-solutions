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

def deleteAtPosition(head, pos):
    #code here
    if not head:
        return head
    if pos == 1:
        if not head.next:
            return None
        return head.next
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    curr.next = curr.next.next
    return head

head = deleteAtPosition(head, 3)
print_linked_list(head)