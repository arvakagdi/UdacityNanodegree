# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.


    if list1 is None:
        return list2
    if list2 is None:
        return list1

    newlist1 = list1.head
    newlist2 = list2.head

    MergedList = LinkedList(None)

    while newlist1 is not None or newlist2 is not None:

        if newlist1 is None:
            MergedList.append(newlist2.value)
            newlist2 = newlist2.next

        elif newlist2 is None:
            MergedList.append(newlist1.value)
            newlist1 = newlist1.next

        elif newlist1.value > newlist2.value:
            MergedList.append(newlist2.value)
            newlist2 = newlist2.next

        else:
            MergedList.append(newlist1.value)
            newlist1 = newlist1.next

    return MergedList

    pass

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(Node(3))
linked_list.append(Node(5))

nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list.append(Node(second_linked_list))
solution = nested_linked_list.flatten()
assert solution == [1,2,3,4,5]




# linked_list = LinkedList(Node(1))
# linked_list.append(3)
# linked_list.append(5)
#
# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)
#
# merged = merge(linked_list, second_linked_list)
# node = merged.head
# while node is not None:
#     # This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next
#
# # Lets make sure it works with a None list
# merged = merge(None, linked_list)
# node = merged.head
# while node is not None:
#     # This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next