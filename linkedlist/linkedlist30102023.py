class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next =next  
class LinkedList:
    def __init__(self, val) -> None:
        self.head = ListNode(val)
    def append(self, val) -> None:
        if not self.head:
            self.head = ListNode(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
    def prepend(self, val) -> None:
        # add node to beginning of list
        root = ListNode(val) 
        root.next = self.head
        self.head = root
    def delete(self, val) -> None:
        if not self.head:
            return;
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return;
    def print(self) -> None:
        if not self.head:
            return;
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

def mergeTwoLists(l1, l2):
    if not l1: return l2
    if not l2: return l1

    dummy = ListNode(0)
    curr = dummy
    # will be leftover
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



        
test = LinkedList(0)
test.append(1)
test.append(2)
test.append(3)
test.print()
# print(test)
test.delete(2)
print("+++++++++++++ \n")
test.print()
# print(test)


