# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list. 
class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self, v): 
        new_node = Node(v)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return True
    
    def append_item(self, v):
        new_node = Node(v)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    

def find_k(x, k):
    head = x.head
    temp = head
    flag = 1
    element_idx = x.length - k +1
    while temp:
        if flag == element_idx:
            return temp.value
        temp = temp.next
        flag +=1
    return False

h = LinkedList(5)
h.append_item(6)
h.append_item(7)
h.append_item(8)
h.append_item(18)
h.append_item(45)
h.append_item(53)
h.append_item(23)
h.print_list()
print(find_k(h, 4))