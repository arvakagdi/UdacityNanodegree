'''
Create a Node class with value and next attributes
Use the class to create the head node with the value 2
Create and link a second node containing the value 1
Try printing the values (1 and 2) on the nodes you created (to make sure that you can access them!)
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

    def print_linked_list(self):

        MyNodes = head

        while MyNodes != None:
            print(MyNodes.value)
            MyNodes = MyNodes.next

    # def addNode (self,value):
    #     MyNodes = head
    #
    #     while MyNodes.next != None:
    #         MyNodes = MyNodes.next
    #     MyNodes.next = Node(value)



def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    MyNodes = None
    for value in input_list:
        if head == None:
            head = Node(value)
        else:
            MyNodes = head
            while MyNodes.next != None:
                MyNodes = MyNodes.next
            MyNodes.next = Node(value)
    return head


def create_linked_list_better(input_list):
    head = None
    tail = None

    for i in input_list:
        if head is None:
            head = Node(i)
            tail = head
        else:
            tail.next = Node(i)
            tail = tail.next

    return head


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)



# #test cases for add function
#
# head = Node(1)
# head.addNode(2)
# head.addNode(3)
# head.print_linked_list()

