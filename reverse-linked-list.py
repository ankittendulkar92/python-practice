class listnode:
  def__init__self(self,x):
    self.val=x
    self.next=None
  def check_reverse(self,head):
    if head==None or head.next==None:
      return head
    else:
      temp=None,Next_head=None
      while head!=None:
        next_head=head.next
        head.next=temp
        temp=head
        head=next_head
      return temp
