# Time:  O(1)
# Space: O(1)
#
# Write a function to delete a node (except the tail) in a singly linked list,
# given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
# with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
