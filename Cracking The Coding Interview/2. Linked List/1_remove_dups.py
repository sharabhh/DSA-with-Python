# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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

        
def find_dups(head):
    curr = head
    while curr:
        runner = curr
        while runner.next:
            if runner.next.value == curr.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return head

h = LinkedList(2)
h.append_list(1)
h.append_list(3)
h.append_list(4)
h.append_list(2)
h.append_list(1)
h.print_list()
print('--------')
print(find_dups(h.head))
h.print_list()