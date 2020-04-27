# this code makes the tree that we'll traverse

class Node(object):

    def __init__(self, value=None):
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

    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert(self, new_node):
        mynode = Node(new_node)
        if self.root.get_value() is None:
            self.set_root(new_node)
            return

        curr_node = self.root

        while True:
            if curr_node is not None:
                if self.compare(curr_node,mynode) == -1:
                    if curr_node.has_left_child() is False:
                        curr_node.set_left_child(mynode)
                        return
                    else:
                        curr_node = curr_node.left


                elif self.compare(curr_node,mynode) == 1:
                    if curr_node.has_right_child() is False:
                        curr_node.set_right_child(mynode)
                        return

                    else:
                        curr_node = curr_node.right
                else:
                    return

    def insert_with_recursion(self,new_node):
        mynode = Node(new_node)
        if self.root.get_value() is None:
            self.set_root(new_node)
            return

        curr_node = self.root
        self.helper(curr_node,mynode)

    def helper(self, curr_node, mynode):
        if self.compare(curr_node, mynode) == -1:
            if curr_node.has_left_child() is False:
                curr_node.set_left_child(mynode)
                return
            else:
                self.helper(curr_node.get_left_child(),mynode)

        elif self.compare(curr_node, mynode) == 1:
            if curr_node.has_right_child() is False:
                curr_node.set_right_child(mynode)
                return
            else:
                self.helper(curr_node.get_right_child(),mynode)
        else:
            return

    def search(self, value):
        if self.root is None:
            return False

        curr_node = self.get_root()
        mynode = Node(value)

        while True:
            comp = self.compare(curr_node,mynode)
            if comp == 0:
                return True
            if comp == -1:
                if curr_node.has_left_child() is False:
                    return False
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.has_right_child() is False:
                    return False
                else:
                    curr_node = curr_node.right


def preorder(node,visited_list):
    if node:
        visited_list.append(node.value)
        preorder(node.get_left_child(),visited_list)
        preorder(node.get_right_child(),visited_list)

    return visited_list

# create a tree and add some nodes
tree = Tree()
# tree.insert(6)
# tree.insert(4)
# tree.insert(10)
# tree.insert(5)
# tree.insert(7)
# tree.insert(12)

tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(10)
tree.insert_with_recursion(5)
tree.insert_with_recursion(7)
tree.insert_with_recursion(12)

print(tree.search(11))


visited_list = list()
root = tree.get_root()
print(preorder(root,visited_list))
