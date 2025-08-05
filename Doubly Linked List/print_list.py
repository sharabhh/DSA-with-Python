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
    
    def prepend_item(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        # print("added to front")

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return True
    
    def get_item(self, index):
        if index < 0 or index > self.length:
            return None
        halfway = round(self.length / 2)
        if index < halfway:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
            return temp
    
    def set_item(self, index, value):
        temp = self.get_item(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert_item(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend_item(value)
        if index == self.length:
            self.append_item(value)

        temp = self.get_item(index)
        if temp:
            new_node = Node(value)
            oldPrev = temp.prev
            temp.prev = new_node
            new_node.prev = oldPrev
            oldPrev.next = new_node
            new_node.next = temp
            self.length += 1
            return True
        return False
    
    def remove_item(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
           return self.pop_first()
        if index == self.length - 1:
            return self.pop_item()
        
        temp = self.get_item(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -=1
        return temp
            


obj1 = DoublyLinekdList(7)
obj1.append_item(2)
obj1.append_item(3)
obj1.append_item(4)
# obj1.pop_first()
# obj1.pop_item()

obj1.print_list()
print("-------")
obj1.remove_item(3)
obj1.print_list()
# print("-------------")
# obj1.set_item(3,9)
# obj1.print_list()
# print(obj1.get_item(3))