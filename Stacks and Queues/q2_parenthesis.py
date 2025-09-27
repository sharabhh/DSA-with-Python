# Check to see if a string of parentheses is balanced or not.
# By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is a balanced string. On the other hand, the string "(()))" has an imbalance, as the last two parentheses do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close parenthesis needs to follow the open parenthesis.
# Your program should take a string of parentheses as input and return True if it is balanced, or False if it is not. In order to solve this problem, use a Stack data structure.

class Stack:
    def __init__(self, value):
        self.stack_list = [value]

    def append_stack(self, value):
        self.stack_list.append(value)
    
    def pop_stack(self):
        if len(self.stack_list) == 0:
            print("Stack is already empty :')")
        else:
            self.stack_list.pop()
        return
    
    def print_stack(self):
        for i in self.stack_list:
            print(i)
        return
    
    def is_balanced(self):
        match_stack = []
        for i in self.stack_list:
            if i == "(" or i== "{" or i == "[":
                match_stack.append(i)
            else:
                if not match_stack:
                    return False
                if i == ")":
                    if match_stack.pop() != "(":
                        return False
                elif i == "}":
                    if match_stack.pop() != "{":
                        return False
                elif i == "]":
                    if match_stack.pop() != "[":
                        return False
        
        # return match_stack
        return not match_stack
            
            
        # return match_stack
    
mystack = Stack("{")
mystack.append_stack("(")
mystack.append_stack("[")
mystack.append_stack("]")
mystack.append_stack(")")
mystack.append_stack("}")
print(mystack.is_balanced())
# mystack.append_stack(5)
# mystack.print_stack()