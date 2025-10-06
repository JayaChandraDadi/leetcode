# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        arr = set(nums)
        prev = None
        temp = head
        while(temp!=None):
            front = temp.next
            if temp.val in arr:
                if prev:
                    prev.next = front
                else:
                    head = front
            else:
                prev = temp
            temp = front
        return head
        
            
        