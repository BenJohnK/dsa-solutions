class Stack:
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)
    
    def pop(self):
        if not self.queue:
            return "Stack is empty"
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)
    
    def top(self):
        if not self.queue:
            return "Stack is empty"
        return self.queue[-1]
    
    def __str__(self):
        return str(self.queue)


s = Stack()
print(s)
s.push(10)
s.push(20)
s.push(30)
print(s)
s.pop()
print(s)
print(s.top())