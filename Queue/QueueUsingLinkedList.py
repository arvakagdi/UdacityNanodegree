class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
'''
Queue class. 
It will need three attributes:

A head attribute to keep track of the first node in the linked list
A tail attribute to keep track of the last node in the linked list
A num_elements attribute to keep track of how many items are in the stack
'''
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    #Enqueue Method
    #If the queue is empty, then both the head and tail should refer to the new node (because when there's only one node, this node is both the head and the tail)
    #Otherwise (if the queue has items), add the new node to the tail (i.e., to the end of the queue)
    #Be sure to shift the tail reference so that it refers to the new node (because it is the new tail)

    def enqueue(self,data):
        LastNode = Node(data)
        if self.head is None:
            self.head = LastNode
            self.tail = self.head

        else:
            self.tail.next = LastNode    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def dequeue(self):
        if self.is_empty():
            return None
        ToReturn = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return ToReturn


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")