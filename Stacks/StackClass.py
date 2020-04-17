class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    # TODO Add the push method
    def push(self,data):
        if self.next_index >= len(self.arr) :
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

        '''
        Add a size method that returns the current size of the stack
        Add an is_empty method that returns True if the stack is empty and False otherwise
        '''

    def size (self):
        return self.num_elements

    def is_empty(self):
        return self.next_index == 0


    def pop(self):
        if self.is_empty():
            return None

        ToPop = self.arr[self.next_index - 1]
        self.arr[self.next_index -1] = None
        self.next_index -= 1
        self.num_elements -= 1

        # self.next_index -= 1    #Easy way
        # self.num_elements -= 1
        # return self.arr[self.next_index]

        return ToPop

    def _handle_stack_capacity_full (self):
        old_arr = self.arr
        self.arr =  [None for _ in range(2* len(old_arr))]

        for i,j in enumerate(old_arr):     # enumerate returns tuples
            self.arr[i] = j


#
# foo = Stack()
# foo.push(1)
# foo.push(2)
# foo.push(1)
# foo.push(2)
# foo.push(1)
# foo.push(2)
# foo.push(1)
# foo.push(2)
# foo.push(1)
# foo.push(2)
# foo.push(1)
# foo.push(2)
# print(foo.arr)

# foo = Stack()
# print(foo.size()) # Should return 0
# print(foo.is_empty()) # Should return True
# foo.push("Test") # Let's push an item onto the stack and check again
# print(foo.size()) # Should return 1
# print(foo.is_empty()) # Should return False


foo = Stack()
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack
