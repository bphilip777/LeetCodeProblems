class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.nextNode = nextNode

def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
    rollover = False
    head = ListNode
    current = head
    while l1 is not None or l2 is not None:
        val = 0
        if l1 is not None:
            val += l1.val
            l1 = l1.nextNode
        if l2 is not None:
            val += l2.val
            l2 = l2.nextNode
        if rollover: # Check if on the previous loop rollover was greater than 10
            val += 1
            rollover = False
        if val > 9:
            rollover = True
            val %= 10
        current.val = val
        # Prepare for next loop
        if l1 is not None or l2 is not None:
            current.nextNode = ListNode(0)
            current = current.nextNode
        else:
            break
    return head

def convertListToListNode(values:list[int]) -> ListNode:
    # Initialize head of list node
    head = ListNode(values[0])
    for i, n in enumerate(values[1:]):
        if i == 0:
            prev = head
        else:
            prev = current
        current = ListNode(n)
        prev.nextNode = current
    return head

def printListNode(ln:ListNode):
    while(ln != None):
        print(ln.val)
        ln = ln.nextNode

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