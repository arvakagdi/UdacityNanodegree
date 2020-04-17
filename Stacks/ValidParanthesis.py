'''
Valid Paranthesis using stack implemented by using list inbuilt functions
'''

class Stack:
    def __init__(self):
        # TODO: Initialize the Stack
        self.items = []

    def size(self):
        # TODO: Check the size of the Stack
        return len(self.items)

    def push(self, item):
        # TODO: Push item onto Stack
        self.items.append(item)

    def pop(self):
        # TODO: Pop item off of the Stack
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """

    # TODO: Intiate stack object
    # TODO: Interate through equation checking parentheses
    # TODO: Return True if balanced and False if not

    MyStack = Stack()

    for symbol in equation:
        if symbol == '(' or symbol == ')':
            MyStack.push(symbol)

        if symbol == ')':
            if MyStack.size() >= 2:
                MyStack.pop()
                MyStack.pop()
            else:
                return False

    return MyStack.size() == 0

###########EASY SOLUTION######################
    # stack = Stack()
    #
    # for char in equation:
    #     if char == "(":
    #         stack.push(char)
    #     elif char == ")":
    #         if stack.pop() == None:
    #             return False
    #
    # if stack.size() == 0:
    #     return True
    # else:
    #     return False


print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")


#Test case for Stack

# MyStack = Stack()
#
# MyStack.push("Web Page 1")
# MyStack.push("Web Page 2")
# MyStack.push("Web Page 3")
#
# print (MyStack.items)
#
# MyStack.pop()
# MyStack.pop()
#
# print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")
#
# MyStack.pop()
#
# print ("Pass" if (MyStack.pop() == None) else "Fail")