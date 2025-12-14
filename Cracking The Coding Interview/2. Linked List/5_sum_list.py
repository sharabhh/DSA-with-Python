'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the Vs digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7- > 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295,
Output:9 -> 1 -> 2,Thatis,912. 

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0
    
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

def sum_ll(x,y):
    left_head = x.head
    right_head = y.head
    new_ll = LinkedList()
    carry = 0

    while left_head or right_head or carry:
        val1 = left_head.value if left_head else 0
        val2 = right_head.value if right_head else 0
        
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10

        new_ll.append_list(digit)

        if left_head:
            left_head = left_head.next
        if right_head:
            right_head = right_head.next

    return new_ll

h = LinkedList()
h.append_list(1)
h.append_list(3)
h.append_list(4)

b = LinkedList()
b.append_list(9)
b.append_list(9)
b.append_list(9)

summed = sum_ll(h,b)
summed.print_list()