'''
Linked lists with multiple functionality
'''


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def to_list(self):
        start = self.head
        MyList = []
        while start:
            MyList.append(start.value)
            start = start.next
        return MyList

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        newnode = None
        if self.head is None:
            self.head = Node(value)

        else:
            newnode = self.head
            self.head = Node(value)
            self.head.next = newnode
        pass

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        newlist = self.head
        while newlist:
            if newlist.value == value:
                return newlist
            else:
                newlist = newlist.next
        pass

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head is None:
            return None

        if self.head.value == value:
            self.head = self.head.next

        else:
            newlist = self.head
            while newlist:
                if newlist.next.value == value:
                    newlist.next = newlist.next.next
                    return
                else:
                    newlist = newlist.next
            pass

    def pop(self):
        """ Return the first node's value and remove it from the list. """

        if self.head is None:
            return None

        value = 0
        value = self.head.value
        self.head = self.head.next
        return value

        pass

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return

        length = self.size()

        newlist = self.head

        if pos > length:
            while newlist.next is not None:
                newlist = newlist.next

            newlist.next = Node(value)

        else:
            newlist = self.head
            i = 1
            addNode = Node(value)
            while newlist:
                if i == pos:
                    addNode.next = newlist.next
                    newlist.next = addNode
                    return
                else:
                    i += 1
                    newlist = newlist.next
        pass

    def size(self):
        """ Return the size or length of the linked list. """

        newlist = self.head
        size = 0

        while newlist:
            size += 1
            newlist = newlist.next

        return size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    ReverseList = LinkedList()
    ReverseList.head = None


    for value in linked_list:
        newnode = Node(value)
        newnode.next = ReverseList.head
        ReverseList.head = newnode

    return ReverseList
    pass


## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
#
# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

#
# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
# #

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"
#
# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# # Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")