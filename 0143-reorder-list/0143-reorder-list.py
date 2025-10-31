# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,temp):
        prev = None
        while(temp!=None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def reorderList(self, head):
        if not head:
            return 
        if head.next==None:
            return head
        slow = head
        fast = head
        prev = None
        while(fast!=None and fast.next!=None):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        temp1 = head
        temp2 = self.reverse(slow)
        while(temp1!=None and temp2!=None):
            front1 = temp1.next
            temp1.next = temp2
            front2 = temp2.next
            temp2.next = front1
            temp1 = front1
            if temp1==None:
                temp2.next = front2
            temp2 = front2
        return head
        
        