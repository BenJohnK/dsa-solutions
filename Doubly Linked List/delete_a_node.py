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

def delPos(head, x):
        # code here
        if not head.next and x == 1:
            return
        if head.next and x == 1:
            head.next.prev = None
            temp = head
            head = head.next
            temp.next = None
            return head
        curr = head
        for i in range(x-2):
            curr = curr.next
            if not curr.next:
                return head
        if curr.next.next:
            curr.next.next.prev = curr
        temp = curr.next
        curr.next = curr.next.next
        temp.prev = None
        temp.next = None
        return head

print_doubly_linked_list(head)

head = delPos(head, 1)

print_doubly_linked_list(head)