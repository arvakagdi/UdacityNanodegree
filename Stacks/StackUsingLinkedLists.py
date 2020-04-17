'''
Complexity O(1) as we all was push or pop data at the head of the linkedlist
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None # No items in the stack, so head should be None
        self.num_elements = 0 # No items in the stack, so num_elements should be 0
    '''
    push method:
    
    The method will need to have a parameter for the value that you want to push
    You'll then need to create a new Node object with this value and link it to the list
    Remember that we want to add new items at the head of the stack, not the tail!
    Once you've added the new node, you'll want to increment num_elements
    '''

    def push(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode
        self.num_elements += 1

    '''
    Add a size method that returns the current size of the stack
    Add an is_empty method that returns True if the stack is empty and False otherwise
    '''

    def size(self):
        return self.num_elements
    def is_empty(self):
        return self.head == None

    '''
    pop method
    Check if the stack is empty and, if it is, return None
    Get the value from the head node and put it in a local variable
    Move the head so that it refers to the next item in the list
    Return the value we got earlier
    '''

    def pop(self):
        if self.head is None:
            return None
        else:
            PopNode = self.head.value
            self.head = self.head.next
            self.num_elements -= 1

            return PopNode


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")