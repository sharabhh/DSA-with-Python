class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1
    
    def print_list(self):
        if self.head is None:
            print("empty list")

        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return
    
    def append_list(self, val):
        new_node = Node(val)
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1
        return True
    
def del_middle_node(n):
    if n is None or n.next is None:
        return False
    n.value = n.next.value
    n.next = n.next.next
    return True

h = LinkedList(2)
h.append_list(1)
h.append_list(3)
h.append_list(4)
h.append_list(2)
h.append_list(1)
h.print_list()
del_middle_node(h.head.next.next)