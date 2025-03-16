# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        tail = head
        length = 1
        if head==None or head.next==None:
            return head
        while(tail.next!=None):
            length+=1
            tail = tail.next
        r = k%length
        init = length-r
        tail.next = head
        ct = 1
        temp = head
        while(ct<init):
            ct+=1
            temp = temp.next
        head = temp.next
        temp.next = None
        return head
        
        