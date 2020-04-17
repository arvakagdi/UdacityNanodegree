'''
our queue has the following functionality:

enqueue - adds data to the back of the queue
dequeue - removes data from the front of the queue
front - returns the element at the front of the queue
size - returns the number of elements present in the queue
is_empty - returns True if there are no elements in the queue, and False otherwise
_handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
Also, if the queue is empty, dequeue and front operations should return None.

'''

class Queue:
    def __init__(self, arr_size = 10):
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
        self.arr = [0 for _ in range(arr_size)]

    def enqueue(self,data):
        if self.queue_size == len(self.arr):
            self._handle_full_capacity()

        self.arr[self.next_index] = data
        self.next_index = (self.next_index + 1) % len(self.arr)     # modulo used as it is a wrap around array
        self.queue_size += 1

        if self.front_index == -1:
            self.front_index += 1

#dequeue - removes data from the front of the queue

    def dequeue(self):
        if self.queue_size == 0:
            return None

        ToPop = self.arr[self.front_index]

        self.queue_size -= 1
        if self.queue_size == 0:
            self.front_index = -1
        else:
            self.front_index = (self.front_index + 1) % len(self.arr)

        return ToPop

    #front - returns the element at the front of the queue

    def size(self):
        return self.queue_size

    def front(self):
        if self.size() == 0:
            return None
        return(self.arr[self.front_index])

    def is_empty(self):
        return self.size() == 0

    def _handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2*len(old_arr))]

        index = 0
        # copy all elements from front of queue (front-index) until end
        for i in range (self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1
        # case: when front-index is ahead of next index
        for i in range(0,self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # Reset Pointers
        self.front_index = 0
        self.next_index = index


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