#In this exercise we are going to create a queue with just stacks.
# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.mylist = Stack()
        self.poplist = Stack()

    def size(self):
        return self.mylist.size() + self.poplist.size()

    def enqueue(self, item):
        self.mylist.push(item)

    def dequeue(self):
        if self.poplist.size() == 0 and self.mylist.size() == 0:
            return None

        if self.poplist.size() == 0:
            while self.mylist.items:
                self.poplist.push(self.mylist.pop())

        return self.poplist.pop()

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")