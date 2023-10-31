class ListNode:
	def __init__(self, val, n=None):
		self.val = val
		self.next = n
class LinkedList:
	def __init__(self, val):
		self.head = ListNode(val)
	def append(self, val):
		temp = ListNode(val)
		if not self.head:
			self.head = temp
			return;
		curr = self.head
		while curr.next:
			curr = curr.next
		curr.next = temp
	def delete(self, val):
	    if not self.head:
	        return
	    if self.head.val == val:
	        self.head = self.head.next
	        return
	    curr = self.head
	    while curr.next:
	        if curr.next.val == val:
	            curr.next = curr.next.next
	            return
            curr = curr.next
	def prepend(self, val):
		temp = ListNode(val)
		temp.next = self.head
		self.head = temp
	def reverseList(self):
		prev = None
		curr = self.head 
		while curr:
			next_node = curr.next ## points to next node now
			curr.next = prev ## points to prev node now  ( the reverse is here mainly)
			prev = curr ## incr prev to next node 
			curr = next_node ##  incr curr to next next node
		return prev
		
			
			
			 

		
