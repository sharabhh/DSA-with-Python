class Stack:
    def __init__(self):
        self.stack_list = []

    def append_stack(self, string):
        for i in string:
            self.stack_list.append(i)
        return

    def reverse_stack(self):
        if len(self.stack_list) == 0:
            print("already empty :')")
            return
        new_string = ""
        while self.stack_list:
            new_string += self.stack_list.pop()
        return new_string

mystack = Stack()
mystack.append_stack("abcde")
print(mystack.reverse_stack())
