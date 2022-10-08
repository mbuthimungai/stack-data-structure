from collections import deque
stack = deque()
MAX_SIZE = 10
class Stack:
    def __init__(self):        
        pass
    def push(self,element):
        if len(stack) != MAX_SIZE:
            stack.appendleft(element)
    def pop(self):
        stack.pop()
    def peek(self):
        return stack[-1]
    def isEmpty(self):
        return len(stack) == 0
    def isFull(self):
        return len(stack) == MAX_SIZE
