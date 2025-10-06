# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head.next==None:
            return 
        slow = head
        fast = head
        while(fast!=None and fast.next!=None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
        