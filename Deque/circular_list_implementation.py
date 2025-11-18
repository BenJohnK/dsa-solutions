class MyDeque:
    def __init__(self, cap):
        self.deque = [None] * cap
        self.cap = cap
        self.front = 0
        self.sz = 0

    def insertRear(self, x):
        if self.sz == self.cap:
            return "Deque is full"
        rear = (self.front + self.sz)%self.cap
        self.deque[rear] = x
        self.sz += 1
        return "inserted"

    def deleteFront(self):
        if self.sz == 0:
            return "Deque is empty"
        self.deque[self.front] = None
        self.front = (self.front + 1)%self.cap
        self.sz -= 1
        return "deleted"

    def insertFront(self, x):
        if self.sz == self.cap:
            return "Deque is full"
        front = (self.front - 1)%self.cap
        self.deque[front] = x
        self.front = front
        self.sz += 1
        return "inserted"
    
    def deleteRear(self):
        if self.sz == 0:
            return "Deque is empty"
        rear = (self.front + self.sz - 1)%self.cap
        self.deque[rear] = None
        self.sz -= 1
    
    def getSize(self):
        return self.sz
    
    def isEmpty(self):
        return self.sz == 0

    def getFront(self):
        return self.deque[self.front] if self.sz > 0 else "Deque is empty"
    
    def getRear(self):
        if self.sz == 0:
            return "Deque is empty"
        rear = (self.front + self.sz - 1)%self.cap
        return self.deque[rear]
    
    def __str__(self):
        return str(self.deque)

q = MyDeque(4)

print(q.insertRear(1))
print(q.insertRear(2))
print(q.insertRear(3))
print(q.insertRear(4))
print(q)
print(q.insertRear(5))
print(q.deleteFront())
print(q)
print(q.getFront())
print(q.getRear())
print(q.getSize())
print(q.insertFront(1))
print(q)
print(q.deleteRear())
print(q)
print(q.deleteRear())
print(q)
print(q.deleteRear())
print(q)
print(q.deleteRear())
print(q)
print(q.deleteRear())
print(q.insertFront(1))
print(q.insertFront(2))
print(q)
print(q.deleteFront())
print(q)