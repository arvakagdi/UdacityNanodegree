class Queue:
    def __init__(self):
        # TODO: Initialize the Queue
        self.mylist = []
        self.num_elements = 0

    def size(self):
        return self.num_elements

    def enqueue(self, item):
        self.mylist.append(item)
        self.num_elements += 1

    def dequeue(self):
        self.num_elements -= 1
        return self.mylist.pop(0)


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