class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
    vals1 = []
    vals2 = []
    while l1 is not None:
        vals1.append(l1.val)
        l1 = l1.next
    while l2 is not None:
        vals2.append(l2.val)
        l2 = l2.next
    # Shift to the correct value
    vals1 = [val * 10**i for i, val in enumerate(vals1)]
    vals2 = [val * 10**i for i, val in enumerate(vals2)]
    # Reverse the arrays
    vals1.reverse()
    vals2.reverse()
    # Add them all together
    vals = [a for a in str(sum(vals1) + sum(vals2))]
    vals.reverse()
    l3 = convertListToListNode(vals)
    return l3

def convertListToListNode(values:list[int]) -> ListNode:
    # Initialize head of list node
    head = ListNode(values[0])
    for i, n in enumerate(values[1:]):
        if i == 0:
            prev = head
        else:
            prev = current
        current = ListNode(n)
        prev.next = current
    return head

def printListNode(ln:ListNode):
    while(ln != None):
        print(ln.val)
        ln = ln.next


# Create your list nodes
l1T = [2, 4, 3]
l2T = [5, 6, 4]

l1 = convertListToListNode(l1T)
l2 = convertListToListNode(l2T)

# printListNode(l1)
# printListNode(l2)

# Check if your algorithm works
l3 = addTwoNumbers(l1, l2)
printListNode(l3)