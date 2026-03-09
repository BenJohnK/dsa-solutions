'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

'''

class MinStack:
    def __init__(self):
        self.lst = []
        self.min_lst = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        if not self.min_lst:
            self.min_lst.append(val)
            return
        if val <= self.min_lst[-1]:
            self.min_lst.append(val)
            return

    def pop(self) -> None:
        x = self.lst.pop()
        if x == self.min_lst[-1]:
            self.min_lst.pop()
            return

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min_lst[-1]
    
