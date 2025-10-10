class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

def sumOfElements(head):
    #code here
    sum = 0
    curr = head
    while curr:
        sum += curr.data
        curr = curr.next
    return sum

print(sumOfElements(head))