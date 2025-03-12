# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        if fast==None:
            return head.next
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
