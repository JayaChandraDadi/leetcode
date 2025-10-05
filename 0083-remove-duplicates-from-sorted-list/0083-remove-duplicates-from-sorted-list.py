# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return 
        left = head
        right = left.next
        while(right!=None):
            if left.val==right.val:
                right = right.next
            else:
                left.next = right
                left = left.next
                right = right.next
        left.next = right
        return head

            