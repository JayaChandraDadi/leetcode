# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hashmap = {}
        temp = headA
        while(temp!=None):
            hashmap[temp] = 1
            temp = temp.next
        temp = headB
        while(temp!=None):
            if temp in hashmap:
                return temp
            else:
                temp = temp.next
        return 
        