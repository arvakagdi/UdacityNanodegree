class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Solution
def even_after_odd(head):
    # helper functions for testing purpose
    oddlist = None
    evenlist = None

    if head is None:
        return None

    while head:
        if head.data%2 == 0:
            if evenlist is None:
                evenlist = head
                evenlist.next = None
                newlist = evenlist
            else:
                newlist.next = head
                newlist = newlist.next
                newlist.next = None
        else:
            if oddlist is None:
                oddlist = head
                oddlist.next = None
                newlistodd = oddlist

            else:
                newlistodd.next = head
                newlistodd = newlistodd.next
                newlistodd.next = None

        head = head.next

    if evenlist is None:
        return oddlist
    if oddlist is None:
        return evenlist

    else:
        evenafteroddlist = oddlist

        while evenafteroddlist.next:
            evenafteroddlist = evenafteroddlist.next
        evenafteroddlist.next = evenlist

        return oddlist

# # Solution
# def even_after_odd(head):
#     if head is None:
#         return head
#
#     even = None
#     odd = None
#     even_tail = None
#     head_tail = None
#
#     while head:
#         next_node = head.next
#
#         if head.data % 2 == 0:
#             if even is None:
#                 even = head
#                 even_tail = even
#             else:
#                 even_tail.next = head
#                 even_tail = even_tail.next
#         else:
#             if odd is None:
#                 odd = head
#                 odd_tail = odd
#             else:
#                 odd_tail.next = head
#                 odd_tail = odd_tail.next
#         head.next = None
#         head = next_node
#
#     if odd is None:
#         return even
#     odd_tail.next = even
#     return odd



def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)


arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)


arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)


arr = [1, 2, 5, 8, 9, 11]
solution = [1, 5, 9, 11, 2, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 5, 8, 9, 11]
solution = [1, 5, 9, 11, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 5, 8, 9, 11, 12]
solution = [5, 9, 11, 2, 4, 8, 12]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)