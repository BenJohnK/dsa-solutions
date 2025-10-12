class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(30)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(20)

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def check_palindrome(head):
    lst = []
    curr = head
    while curr:
        lst.append(curr.data)
        curr = curr.next
    i = 0
    j = len(lst) - 1
    while(i<j):
        if lst[i] != lst[j]:
            return False
        i += 1
        j -= 1
    else:
        return True

print(check_palindrome(head))