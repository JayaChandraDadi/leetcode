# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        temp = head
        arr = []
        if head==None or head.next==None:
            return head
        while(temp!=None and temp.next!=None):
            arr.append(temp.val)
            temp = temp.next.next
        if temp!=None:
            arr.append(temp.val)
        temp = head.next
        while(temp.next!=None and temp!=None and temp.next.next!=None):
            arr.append(temp.val)
            temp = temp.next.next
        if temp!=None:
            arr.append(temp.val)
        temp=head
        i = 0
        for i in range(len(arr)):
            temp.val = arr[i]
            temp = temp.next
        return head




        