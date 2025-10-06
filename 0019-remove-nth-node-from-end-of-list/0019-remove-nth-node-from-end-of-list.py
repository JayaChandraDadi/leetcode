# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        length = 0
        while(temp!=None):
            length+=1
            temp = temp.next
        if length==1:
            return 
        temp = head
        prev = None
        element = length-n
        ct = 0
        if element==0:
            head = temp.next
            temp.next=None
            return head  
        while(temp!=None):
            ct+=1
            prev = temp
            temp = temp.next
            if ct==element:
                prev.next = temp.next
                break
        return head
