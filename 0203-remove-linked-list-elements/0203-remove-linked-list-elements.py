# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        temp = head
        prev = dummy
        while(temp!=None):
            front = temp.next
            if temp.val==val:
                temp.next = None
                prev.next = front
                temp = front
            else:
                prev = temp
                temp = front
        return dummy.next