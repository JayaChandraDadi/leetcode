# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head):
        if head==None or head.next==None:
            return head
        temp = head.next
        prev = None
        while(temp!=None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def isPalindrome(self, head):
        slow = head
        fast = head
        if head==None:
            return True
        
        while(fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next
        #reverse of ll
        newhead = self.reverse(slow)
        temp = head
        while(newhead!=None):
            if temp.val==newhead.val:
                newhead = newhead.next
                temp = temp.next
            else:
                self.reverse(newhead)
                return False
        temp = self.reverse(newhead)
        return True

        