'Given that the DLL will be circular and will contain odd number of nodes'

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
head.next.next.next = head

def findMiddle(head):
    #code here
    slow = head.next
    fast = head
    while fast.next.next.next!=head:
        slow = slow.next
        fast = fast.next.next
    return slow.data

print(findMiddle(head))