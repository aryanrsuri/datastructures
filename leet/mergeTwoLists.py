class ListNode:
    def __init__(self, val=0, n=None) -> None:
        self.val= val
        self.next = n;


def mergeTwoLists(l1,l2):
        return 
        return 
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1.val
            l1 = l1.next
        else:
            curr.next = l2.val
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return dummy.next
    
