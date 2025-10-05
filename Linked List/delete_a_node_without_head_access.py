'''This is a program to illustrate how to delete a node when only a pointer to the node is given and the head of the linked list is not available'''

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


def delete_node(pointer: Node):
    '''This method wont work if pointer is not the last node'''
    pointer.data = pointer.next.data
    pointer.next = pointer.next.next


pointer = head.next
delete_node(head)
print_linked_list(head)
    
