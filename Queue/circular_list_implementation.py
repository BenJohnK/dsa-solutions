class MyQueue:
    def __init__(self, cap):
        self.queue = [None] * cap
        self.cap = cap
        self.sz = 0
        self.front = 0

    def enqueue(self, x):
        if self.sz == self.cap:
            return "Queue is full"
        rear = (self.front + self.sz)%self.cap
        self.queue[rear] = x
        self.sz += 1
        return "inserted"

    def dequeue(self):
        if self.sz == 0:
            return "Queue is empty"
        self.queue[self.front] = None
        self.front = (self.front + 1)%self.cap
        self.sz -= 1
        return "removed"
    
    def __str__(self):
        return str(self.queue)

    def get_size(self):
        return self.sz
    
    def get_front(self):
        return self.queue[self.front]
    
    def get_rear(self):
        if self.sz == 0:
            return None
        return self.queue[(self.front + self.sz - 1)%self.cap]


q = MyQueue(4)

print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q)
print(q.enqueue(5))
print(q.dequeue())
print(q)
print(q.get_front())
print(q.get_rear())
print(q.get_size())