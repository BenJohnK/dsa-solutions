class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0
    
    def enqueue(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.sz += 1
    
    def size(self):
        return self.sz

    def dequeue(self):
        if not self.head:
            return "Queue is empty"
        temp_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.sz -= 1
        return temp_data
    
    def get_front(self):
        if not self.head:
            return "Queue is empty"
        return self.head.data
    
    def get_rear(self):
        if not self.head:
            return "Queue is empty"
        return self.tail.data

    def is_empty(self):
        if self.sz == 0:
            return True
        return False


q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.size())
q.enqueue(40)
print(q.get_front())
print(q.get_rear())
print(q.is_empty())