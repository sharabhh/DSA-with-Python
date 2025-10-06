# You are given a class MyQueue which implements a queue using two stacks. Your task is to implement the enqueue method which should add an element to the back of the queue.
# To achieve this, you can use the two stacks stack1 and stack2. Initially, all elements are stored in stack1 and stack2 is empty. In order to add an element to the back of the queue, you need to first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.
# Once all elements have been transferred to stack2, push the new element onto stack1. Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.
# Your implementation should satisfy the following constraints:
# The method signature should be def enqueue(self, value).
# The method should add the element value to the back of the queue.

class Stack:
    def __init__(self):
        self.stack_list = []

    def append_stack(self, value):
        self.stack_list.append(value)
        return
    
    def pop_stack(self):
        if len(self.stack_list) == 0:
            print("Stack is empty :')")
            return
        return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def print_stack(self):
        for i in reversed(self.stack_list):
            print(i)
        return
    
    def enqueue(self, value):
        new_stack = Stack()
        while not self.is_empty():
            new_stack.append_stack(self.pop_stack())
        self.append_stack(value)

        while not new_stack.is_empty():
            self.append_stack(new_stack.pop_stack())
        return

mystack = Stack()
mystack.append_stack(1)
mystack.append_stack(2)
mystack.append_stack(3)
mystack.append_stack(4)
# mystack.enqueue(5)
mystack.print_stack()