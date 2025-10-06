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