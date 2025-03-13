# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        t1 = headA
        t2 = headB
        while(t1!=t2):
            if t1.next==None and t2.next==None:
                return
            if t1.next==None:
                t1 = headB
                t2 = t2.next
            elif t2.next==None:
                t2 = headA
                t1 = t1.next
            else:
                t1 = t1.next
                t2 = t2.next
        return t1

        