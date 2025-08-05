class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinekdList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_item(self, value):
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length +=1
        print(f"The new length is {self.length}")
        return True
    
    def pop_item(self):
        if self.head is None:
            print("Already empty list")
            return False
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        
        print(f"New length is {self.length}")
        return temp


obj1 = DoublyLinekdList(7)
obj1.append_item(2)
obj1.append_item(3)
obj1.append_item(4)
obj1.pop_item()

obj1.print_list()