class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        return
    
    def insert_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        level = 1
        while temp is not None:
            if temp.value == value:
                print(f"found at level {level}")
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
            level +=1
        print("value not found")
        return False

my_tree = BinarySearchTree()
my_tree.insert_node(2)
my_tree.insert_node(5)
my_tree.insert_node(1)

my_tree.contains(5)
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)