from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val= val
        self.next = next;

class LinkedList:
    def __init__(self) -> None:
        self.head =None
    def append(self, val):
        # if list is null, val is head node
        if not self.head:
            self.head = ListNode(val)
            return
        # otherwise we traverse through list and add a new node 
        curr = self.head
        while curr.next != None:
            curr = curr.next
        # now we add val to end of the list
        curr.next = ListNode(val)
    def prepend(self, val):
        new = ListNode(val)
        new.next = self.head
        self.head = new
    def delete(self, val):
        if not self.head:
            return 
        if self.head.val == val:
            self.head = self.head.next
            return 

        curr = self.head;
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next


def mergeTwoLists(l1, l2): 
    new = ListNode(0)
    curr = new
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    return new.next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode
                                                      :
    rev = None
    curr = head #1 .. 2
    while curr:
        nextn = curr.next #2 | None
        print(nextn)
        curr.next = prev #None | 1 .. NOne
        print(curr.next)
        prev = curr  #1 .. None | 2next1  
        curr = nextn # 2 | None

    return prev 


s = {"a": 1}
s.get
for i,j in s.items():
    print (i,j)


