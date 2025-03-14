# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2
        dummynode = ListNode(-1)
        curr = dummynode
        carry = 0
        while(t1!=None or t2!=None):
            sum1 = 0
            sum1+=carry
            if t1!=None:
                sum1+=t1.val
            if t2!=None:
                sum1+=t2.val
            newnode = ListNode(sum1%10)
            carry = sum1/10
            curr.next = newnode
            curr = curr.next
            if t1!=None:
                t1 = t1.next
            if t2!=None:
                t2 = t2.next
        if carry>0:
            newnode = ListNode(carry)
            curr.next = newnode
            return dummynode.next
        return dummynode.next
