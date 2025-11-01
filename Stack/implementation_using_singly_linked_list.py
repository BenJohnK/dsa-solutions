class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.sz = 0
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.sz += 1

    def peek(self):
        if not self.head:
            return "Stack is empty"
        return self.head.data
    
    def size(self):
        return self.sz

    def pop(self):
        if not self.head:
            return "Stack is empty"
        temp = self.head.data
        self.head = self.head.next
        self.sz -= 1
        return temp


s1 = Stack()

s1.push(10)
s1.push(20)

print(s1.peek())
