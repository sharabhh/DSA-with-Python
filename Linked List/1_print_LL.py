class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None

        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return new_node
        
        new_node.next = self.head
        self.head = new_node
        self.length +=1
        return new_node
    
    def pop_first(self):
        # if there are no value
        if self.length == 0:
            print("list is already empty")
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -=1
            return

    def get_item(self, index):
        if (index < 0 or index > self.length):
            print("out of range index")
            return None
        
        temp = self.head
        i = 0
        for _ in range(index):
            temp = temp.next
        print(f"The item at {index} is {temp.value}")
        return temp
    
    def set_item(self, index, value):
        temp = self.get_item(index)

        if temp:
            temp.value = value
            return True
        return False

    def insert_node(self, index, value):
        
        if (index < 0 or index > self.length):
            print("out of bound range")
            return False
        
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get_item(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove_item(self, index):
        if (index <0 or index > self.length):
            print("range out of bound")
            return False
        
        if index == 0:
            return self.pop_first()

        if index == self.length:
            return self.pop()
        
        prev_node = self.get_item(index-1)
        temp = prev_node.next

        prev_node.next = temp.next
        temp.next = None
        self.length -= 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        return True
        
py = LinkedList(2)
py.append(3)
# py.append(4)
# py.append(1)
py.append(7)
py.append(7)
# py.prepend(9)
# py.pop_first()
py.print_list()
# py.get_item(1)
# py.set_item(1, 8)
py.insert_node(1, 19)
py.print_list()
# py.remove_item(1)
py.reverse()
py.print_list()

print(f"length is: {py.length}")