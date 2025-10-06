# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findmid(self,head):
        if head==None or head.next==None:
            return head
        slow = head
        fast = head.next
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self,left,right):
        dummynode = ListNode(-1)
        temp = dummynode
        while(left!=None and right!=None):
            if left.val<=right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left:
            temp.next = left
        else:
            temp.next = right
        return dummynode.next
    def mergesort(self,head):
        if not head or head.next==None:
            return head
        middle = self.findmid(head)
        right = middle.next
        middle.next = None
        left = head
        left = self.mergesort(left)
        right = self.mergesort(right)
        return self.merge(left,right)
    def sortList(self, head):
        return self.mergesort(head)