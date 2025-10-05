# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head
        temp1 = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        temp = slow
        prev = None
        while(temp!=None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        temp2 = prev
        while(temp1!=None and temp2!=None):
            if temp1.val==temp2.val:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False
        return True

