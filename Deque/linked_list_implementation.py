class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None
    

class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def insertFront(self, x):
        new_node = Node(x)
        new_node.next = self.head
        if not self.head:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.sz += 1
    
    def insertRear(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.sz += 1
    
    def deleteFront(self):
        if not self.head:
            return "Deque is empty"
        temp = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        self.sz -= 1
        return temp

    def deleteRear(self):
        if not self.head:
            return "Deque is empty"
        if self.head == self.tail:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.sz -= 1
            return temp
        temp = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.sz -= 1
        return temp

    def getSize(self):
        return self.sz

    def getFront(self):
        return self.head.data if self.head else "Deque is empty"

    def getRear(self):
        return self.tail.data if self.tail else "Deque is empty"

    def isEmpty(self):
        return self.head is None


q = MyDeque()

q.insertFront(10)
q.insertFront(5)
q.insertFront(1)

print(q.getFront())
print(q.getRear())
print(q.insertRear(20))
print(q.getFront())
print(q.getRear())
print(q.deleteFront())
print(q.getFront())