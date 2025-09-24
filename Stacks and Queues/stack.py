class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push_stack(self, value):
            
        new_node = Node(value)
        if(self.height == 0):
            self.top = new_node
            return
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return
    
    def pop_stack(self):
        if(self.height == 0):
            print("Stack is empty :')")
            return

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return


    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(5)
my_stack.push_stack(2)
my_stack.push_stack(1)
my_stack.push_stack(26)
my_stack.print_stack()
print('----')
my_stack.pop_stack()
my_stack.pop_stack()
my_stack.pop_stack()
my_stack.pop_stack()
my_stack.pop_stack()
my_stack.print_stack()