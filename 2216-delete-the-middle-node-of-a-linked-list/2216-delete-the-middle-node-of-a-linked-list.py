# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        fast = head
        slow = head
        if head==None or head.next==None:
            return 
        while(fast!=None and fast.next!=None):
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = temp.next.next
        return head
        