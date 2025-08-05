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
            self.length +=1
        else:
            self.head = new_node
            self.tail = new_node
        self.length +=1
        print(f"The new length is {self.length}")
        return True

obj1 = DoublyLinekdList(7)
obj1.append_item(2)

obj1.print_list()