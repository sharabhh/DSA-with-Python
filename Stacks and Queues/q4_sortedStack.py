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
    
    def peek(self):
        if len(self.stack_list) == 0:
            print("Stack is empty :')")
            return
        return self.stack_list[-1]

    def print_stack(self):
        for i in reversed(self.stack_list):
            print(i)
        return
    

def sort_stack(stack):
    sorted_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop_stack()

        # Move elements from sorted_stack back to stack
        # until we find the right spot for temp
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
            stack.append_stack(sorted_stack.pop_stack())

        sorted_stack.append_stack(temp)

    # Move back to original stack so it ends up sorted
    while not sorted_stack.is_empty():
        stack.append_stack(sorted_stack.pop_stack())

    return stack
        

mystack = Stack()
mystack.append_stack(2)
mystack.append_stack(5)
mystack.append_stack(3)
mystack.append_stack(1)
mystack.append_stack(4)
mystack.print_stack()
sort_stack(mystack)
print("---")
mystack.print_stack()
        
