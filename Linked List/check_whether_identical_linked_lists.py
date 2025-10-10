class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(20)

head2 = Node(10)
head2.next = Node(20)
head2.next.next = Node(30)

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


def areIdentical(head1, head2):
        # Code here
        curr1 = head1
        curr2 = head2
        while curr1:
            if (curr1.data != curr2.data) or (curr1.next == None and curr2.next != None) or (curr2.next == None and curr1.next!=None):
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True

print(areIdentical(head1, head2))