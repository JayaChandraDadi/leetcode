# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mid(self,head):
        if head==None or head.next==None:
            return head
        slow = head
        fast = head.next
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergesort(self,left,right):
        dummy = ListNode(-1)
        temp = dummy
        while(left!=None and right!=None):
            if left.val<=right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left!=None:
            temp.next = left
        else:
            temp.next = right
        return dummy.next
    def merge(self,head):
        if head==None or head.next==None:
            return head
        middle = self.mid(head)
        lefthead = head
        righthead = middle.next
        middle.next = None
        lefthead = self.merge(lefthead)
        righthead = self.merge(righthead)
        newhead = self.mergesort(lefthead,righthead)
        return newhead
    def sortList(self, head):
         head = self.merge(head)
         return head

        