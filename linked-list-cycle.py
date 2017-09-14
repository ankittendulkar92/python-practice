class listnode:
	def__init__self(self,x):
		self.val=x
		self.next=None
def Find_cycle(self,x):
	head=x
	if head==None:
		return False
	else:
		fast=head
		slow=head
	while fast!=None and Fast.next!=None:
		slow=slow.next
		fast=fast.next.next
		if fast==slow:
			break

	if fast==None or fast.next==None:
		return False
	elif fast==slow:
		return True

	return False
