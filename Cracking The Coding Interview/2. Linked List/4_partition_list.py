# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions. 
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

def partition_list(ll, x):
    curr = ll.head
    left_head = left_tail = None
    right_head = right_tail = None

    while curr:
        next_node = curr.next
        curr.next = None

        if curr.value < x:
            if left_head is None:
                left_head = curr
                left_tail = curr
            else:
                left_tail.next = curr
                left_tail = curr
        else:
            if right_head is None:
                right_head = curr
                right_tail = curr
            else:
                right_tail.next = curr
                right_tail = curr

        curr = next_node
    if left_head is None:
        ll.head = right_head
        ll.tail = right_tail
        return ll
    
    left_tail.next = right_head
    ll.head = left_head
    ll.tail = right_tail if right_tail else left_tail
    return ll



h = LinkedList()
h.append_list(1)
h.append_list(4)
h.append_list(3)
h.append_list(2)
h.append_list(5)
h.append_list(2)
h.print_list()
print('---')
partition_list(h, 4)
h.print_list()