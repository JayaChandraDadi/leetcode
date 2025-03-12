# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head==None or head.next==None:
            return 
        fast = head.next.next
        slow = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
        