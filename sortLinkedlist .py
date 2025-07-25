"""Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL
Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL """

 # Create a hard-coded linked list:
    # 1 -> 1 -> 2 -> 1 -> 0 -> NULL
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)

curr = head
first0 = None
first1 = None
first2 = None
ptr0 = None
ptr1 = None
ptr2 = None
while curr:
    if curr.data == 0:
        if not ptr0:
            ptr0 = curr
            first0 = ptr0
        else:
            ptr0.next = curr
            ptr0 = ptr0.next
    elif curr.data == 1:
        if not ptr1:
            ptr1 = curr
            first1 = ptr1
        else:
            ptr1.next = curr
            ptr1 = ptr1.next
    elif curr.data == 2:
        if not ptr2:
            ptr2 = curr
            first2 = ptr2
        else:
            ptr2.next = curr
            ptr2 = ptr2.next
    curr = curr.next

if ptr0:
    ptr0.next = first1 or first2
if ptr1:
    ptr1.next = first2
if ptr2:
    ptr2.next = None

head = first0 or first1 or first2




def print_list(node):
    while node is not None:
        print(f" {node.data}", end='')
        node = node.next
    print("\n")

print_list(head)