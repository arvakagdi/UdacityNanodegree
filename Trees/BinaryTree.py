## Define a node

class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    # add set_value and get_value functions
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    ## your code here
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    ## your code here
    def has_left_child(self):
        return self.get_left_child() != None

    def has_right_child(self):
        return self.get_right_child() != None



# define a Tree class here
class Tree(object):
    def __init__(self, value = None):
        self.root = Node(value)
    def get_root(self):
        return self.root



## check

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

