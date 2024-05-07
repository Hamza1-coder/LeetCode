from typing import Optional
import sys
sys.set_int_max_str_digits(86000)

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
def list_to_linkedlist(lst):
    current = dummy = ListNode(0)
    for e in lst:
        current.next = ListNode(e)
        current = current.next
        
    return dummy.next

def traverse_linkedlist(head: Optional[ListNode]):
    while head:
        print(head.val)
        head = head.next
        
def search_element(head: Optional[ListNode], value: int):
    while head:
        if (head.val == value):
            return 1
        head = head.next
    return 0

def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    # reverse the Linkded List
    prev = None
    cur = head
    while (cur != None):
        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    
    # create ans List
    newHead = prev.val
    maxVal = newHead.val
    cur = prev.next

    while(cur!=None):
        if cur.val >= maxVal:
            node = cur.val
            node.next = newHead
            newHead = node
            maxVal = node.val
        cur = cur.next

    return newHead

def doubleIt(head: Optional[ListNode]) -> Optional[ListNode]:
    a = ""
    temp = head
    while head:
        a+=str(head.val)
        head = head.next
    a = str(int(a) * 2)
    temp1 = temp
    for i in a:
        temp.next = ListNode(int(i))
        temp = temp.next
    return temp1.next

    



LL = list_to_linkedlist([9,9,9])
# traverse_linkedlist(LL)
DL = doubleIt(LL)
traverse_linkedlist(DL)

# print(search_element(LL, 5))