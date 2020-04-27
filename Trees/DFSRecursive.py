class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree(object):
    def __init__(self, value = None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def set_root(self,value):
        self.root = Node(value)

def preorder(node,visited_list):
    if node:
        visited_list.append(node.value)
        preorder(node.get_left_child(),visited_list)
        preorder(node.get_right_child(),visited_list)

    return visited_list


def InOrder(node, visited_list):
    if node:
        InOrder(node.get_left_child(),visited_list)
        visited_list.append(node.value)
        InOrder(node.get_right_child(),visited_list)

    return visited_list

def PostOrder(node, visited_list):
    if node:
        PostOrder(node.get_left_child(),visited_list)
        PostOrder(node.get_right_child(),visited_list)
        visited_list.append(node.value)

    return visited_list


from collections import deque



# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

visited_list = list()
root = tree.get_root()
print(InOrder(root,visited_list))




