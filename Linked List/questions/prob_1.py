'''Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:
1 -> 2 -> 3 -> 4
If k=1 then return the first node from the end (the last node) which contains the value of 4.
If k=2 then return the second node from the end which contains the value of 3, etc.
If the index is out of bounds, the program should return None.
The find_kth_from_end function should follow these requirements:
The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
The fast pointer should move k nodes ahead in the list.
If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
The function should return the slow pointer, which will be at the k-th position from the end of the list. '''

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

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
        self.length += 1
        return True
    
    def node_length(self):
        print(self.length)
        return
    
    def find_from_end(self, idx):
        if idx > self.length:
            print("out of bound")
            return False

        temp = self.head

        for _ in range(self.length - idx):
            temp = temp.next
        
        print(f"The number at the position {idx} from end is {temp.value}")

py = LinkedList(2)
py.append(3)
py.append(4)
py.append(5)
py.append(6)
py.node_length()
py.find_from_end(2)