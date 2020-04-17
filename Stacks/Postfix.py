'''
Goal : Given a postfix expression as input, evaluate and return the correct final answer.
Input: List containing the postfix expression
Output: int: Postfix expression solution

Example: 3 1 + 4 *
Solution: (3 + 1) * 4 = 16
'''

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def evaluate_post_fix(input_list):
    # TODO: Iterate over elements
    # TODO: Use stacks to control the element positions
    stack = Stack()

    for elem in input_list:
        if (elem != '+') and (elem != '-') and  (elem != '/') and (elem != '*'):
            stack.push(elem)
        else:
            data2 = stack.top()
            stack.pop()
            data1 = stack.top()
            stack.pop()

            if elem == '+':
                stack.push(int(data1) + int(data2))

            elif elem == '-':
                stack.push(int(data1) - int(data2))

            elif elem == '/':
                stack.push(int(int(data1) / int(data2)))

            elif elem == '*':
                stack.push(int(data1) * int(data2))

    return stack.top()


def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)