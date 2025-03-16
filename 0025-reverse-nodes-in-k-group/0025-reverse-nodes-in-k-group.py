# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findkthnode(self,temp,k):
        k-=1
        while(temp!=None and k>0):
            k-=1
            temp = temp.next
        if temp==None:
            return None
        else:
            return temp
    def reverse(self,head):
        temp = head
        prev = None
        while(temp!=None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def reverseKGroup(self, head, k):
        temp = head
        prev = None
        while(temp!=None):
            kthnode = self.findkthnode(temp,k)
            if kthnode==None:
                if prev!=None:
                    prev.next = temp
                break
            nextnode = kthnode.next
            kthnode.next = None
            self.reverse(temp)
            if temp==head:
                head = kthnode
            else:
                prev.next = kthnode
            prev = temp
            temp = nextnode
        return head


