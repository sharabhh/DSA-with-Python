'''
Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jt h node of the second
linked list, then they are intersecting. 
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(l1):
    length = 0
    while l1:
        length +=1
        l1= l1.next
    return length

def intersection(ll1, ll2):
    length1 = get_length(ll1)
    length2 = get_length(ll2)

    if length1 > length2:
        for _ in range(length1 - length2):
            ll1 = ll1.next
    else:
        for _ in range(length2 - length1):
            ll2 = ll2.next

    while ll1 and ll2:
        if ll1 is ll2:
            print(f"This node is intersecting one: ", ll1)
            return ll1
        ll1 = ll1.next
        ll2 = ll2.next
    print('no intersecting node')
    return False


n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(5)

o1 = ListNode(6)
o2 = ListNode(7)

n1.next = n2
n2.next = n3

o1.next = o2
o2.next = n2

intersection(n1, o1)
print(n2)