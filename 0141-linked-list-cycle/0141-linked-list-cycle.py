# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        temp = head
        mapp = {}
        while(temp!=None):
            if temp in mapp:
                return True
            mapp[temp] = 1
            temp = temp.next
        return False

        