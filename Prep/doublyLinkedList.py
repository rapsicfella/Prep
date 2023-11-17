#this is to implement doubly linked list and to check singular/circular linked lists
class DoublyLinkedList(object):
    def __init__(self, value) -> None:
        self.value = value
        self.nextnode = None
        self.prevnode = None

def cycleCheck(head):
    temp = head
    while not temp == None:
        temp = temp.nextnode
        if temp == head: return True
    return False

def cycleCheck2(head):  #Circular check with 2 ponter race
    s1 = head
    s2 = head
    while s1 != None and s2.nextnode!= None:
        s1 = s1.nextnode
        s2 = s2.nextnode.nextnode
        if s1 == s2 : return True
    return False

def reverse(head):
    cur = head
    prev= temp = None
    while cur:
        temp = cur.nextnode
        cur.nextnode = prev
        prev = cur
        cur = temp
    return prev

def nthToLast(head, n):
    blockst = blockend = head
    #create a block with length n and move that block all over the ll
    #  if blockend reach end, blockstart is our node
    for i in range(n-1):
        if not blockend.nextnode:
            raise LookupError("Error: n is larger than the ll")
        blockend = blockend.nextnode

    while blockend.nextnode:
        blockst = blockst.nextnode
        blockend = blockend.nextnode
    return blockst


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.nextnode = b
b.nextnode = c
#c.nextnode = a #circular 
#b.prevnode = a
#c.prevnode = b
print(cycleCheck(a))
print(cycleCheck2(a))
head = a
print(nthToLast(head, 3).value)
newhead = reverse(head)
print(newhead.value)

