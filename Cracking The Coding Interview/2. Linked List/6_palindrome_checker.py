# Palindrome: Implement a function to check if a linked list is a palindrome. 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_ll(head):
    temp = head
    new_head = None
    while temp:
        new_node = ListNode(temp.val)
        new_node.next = new_head
        new_head = new_node
        temp = temp.next
    return new_head

def compare_nodes(h):
    temp = h
    reversed_ll = reverse_ll(h)
    while temp:
        if temp.val != reversed_ll.val:
            return False
        temp = temp.next
        reversed_ll = reversed_ll.next
    return True

n1 = ListNode(12)
n2 = ListNode(3)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(compare_nodes(n1))