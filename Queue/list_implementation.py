
class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.queue = []
        self.size = n

    def is_empty(self):
        # Check if queue is empty
        if not self.queue:
            return True
        return False

    def isFull(self):
        # Check if queue is full
        if len(self.queue) == self.size:
            return True
        return False

    def enqueue(self, x):
        # Enqueue
        if len(self.queue) == self.size:
            return
        self.queue.append(x)
    
    def dequeue(self):
        # Dequeue
        return self.queue.pop(0)
    
    def get_front(self):
        # Get front element
        if not self.queue:
            return -1
        return self.queue[0]
    
    def get_rear(self):
        # Get rear element 
        if not self.queue:
            return -1
        return self.queue[-1]
        
q = myQueue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
q.enqueue(40)
print(q.get_front())
print(q.get_rear())
print(q.is_empty())