# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        temp = head2
        prev = None
        while(temp!=None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        temp1 = head
        temp2 = prev
        max1 = float('-inf')
        while(temp1!=None and temp2!=None):
            max1 = max(max1,temp1.val + temp2.val)
            temp1 = temp1.next
            temp2 = temp2.next
        return max1