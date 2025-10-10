class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

def maximum(head):
    #code here
    curr = head
    low = None
    while curr:
        if not low or low < curr.data:
            low = curr.data
        curr = curr.next
    return low
    
def minimum(head):
    #code here
    import sys
    low = sys.maxsize
    curr = head
    while curr:
        if curr.data < low:
            low = curr.data
        curr = curr.next
    return low

print(maximum(head), minimum(head))
