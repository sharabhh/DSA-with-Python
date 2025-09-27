# Add a method to declare, push and pop a value onto the Stack implementation with list under the hood.

class Stack:
    def __init__(self, value):
        self.stack_list = [value]

    def push_stack(self, value):
        self.stack_list.append(value)
        return
    
    def pop_stack(self):
        if len(self.stack_list) == 0:
            print("Stack is already empty :')")
        else:
            self.stack_list.pop()
        return

    def print_stack(self):
        for i in reversed(self.stack_list):
            print(i)
        return

mystack = Stack(2)
mystack.push_stack(4)
mystack.push_stack(3)
mystack.push_stack(1)
mystack.push_stack(9)
# mystack.print_stack()
mystack.pop_stack()
mystack.print_stack()