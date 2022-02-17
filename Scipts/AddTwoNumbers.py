class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.nextNode = nextNode

def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
    head = ListNode()
    if type(l1) is not ListNode or type(l2) is not ListNode:
        return head
    rollover = False
    current = head
    while l1 or l2:
        if l1:
            current.val += l1.val
            l1 = l1.nextNode
        if l2:
            current.val += l2.val
            l2 = l2.nextNode
        if rollover:  # Check if on the previous loop rollover was greater than 10
            current.val += 1
            rollover = False
        if current.val > 9:
            rollover = True
            current.val -= 10
        # Prepare for next loop
        if l1 or l2:  # Are there more values?
            current.nextNode = ListNode()
            current = current.nextNode
        elif rollover:  # Was there a rollover?
            current.nextNode = ListNode(1)
            break
        else:  # Exit
            break
    return head

# Way less memory since everything is done in one loop instead
def addTwoNumbersLowMemory(l1:ListNode, l2:ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 or l2
    head = ListNode()
    cur = head
    carry, val = 0, 0
    while l1 or l2 or carry:
        val = carry
        val += l1.val if l1 else 0
        val += l2.val if l2 else 0
        carry = 1 if val > 9 else 0
        val -= 10 if carry else 0
        cur.nextNode = ListNode(val)
        cur = cur.nextNode
        l1 = l1.nextNode if l1 else None
        l2 = l2.nextNode if l2 else None
    return head.nextNode

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
    strs = ''
    while ln is not None:
        strs += str(ln.val)
        ln = ln.nextNode
    print(strs)

# Test cases
l1T = [2, 4, 3]
l2T = [5, 6, 4]
list1 = convertListToListNode(l1T)
list2 = convertListToListNode(l2T)
list3 = addTwoNumbers(list1, list2)
list4 = addTwoNumbersLowMemory(list1, list2)
printListNode(list4)

'''
# Check again
l1T = [0]
l2T = [0]
list1 = convertListToListNode(l1T)
list2 = convertListToListNode(l2T)
list3 = addTwoNumbers(list1, list2)
printListNode(list3)

l1T = [9,9,9,9,9,9,9]
l2T = [9,9,9,9]
list1 = convertListToListNode(l1T)
list2 = convertListToListNode(l2T)
list3 = addTwoNumbers(list1, list2)
printListNode(list3)

# My solution was faster than 32.31% of submissions + less memory intensive than 96.8% of users
# Simply exchanging modulo for subtract improved performance
# Simply swapping head rather than re-instancing it improved speed by so much!
# Apparently doing head = current = Listnode is much slower than doing head = listnode; current = listnode - maybe the way they speed up the code?
'''