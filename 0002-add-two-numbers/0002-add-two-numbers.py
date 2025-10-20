# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp1 = l1
        temp2 = l2
        dummynode = ListNode(-1)
        temp = dummynode
        carry = 0
        while(temp1!=None and temp2!=None):
            sum1 = temp1.val + temp2.val + carry
            remainder = sum1%10
            carry = sum1//10
            temp.next = ListNode(remainder)
            temp1 = temp1.next
            temp2 = temp2.next
            temp = temp.next
        while(temp1!=None):
            sum1 = temp1.val+carry
            remainder = sum1%10
            carry = sum1//10
            temp.next = ListNode(remainder)
            temp1 = temp1.next
            temp = temp.next
        while(temp2!=None):
            sum1 = temp2.val+carry
            remainder = sum1%10
            carry = sum1//10
            temp.next = ListNode(remainder)
            temp2 = temp2.next
            temp = temp.next
        if carry!=0:
            temp.next = ListNode(carry)
            
        return dummynode.next
