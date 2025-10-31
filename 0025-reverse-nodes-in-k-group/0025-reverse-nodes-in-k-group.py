# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def findkthnode(self,temp,k):
        k-=1
        while(temp!=None and k>0):
            temp = temp.next
            k-=1
        return temp
    def reverse(self,temp):
        prev = None
        while(temp!=None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
    def reverseKGroup(self, head, k):
        temp = head
        prevnode = None
        while(temp!=None):
            kthnode = self.findkthnode(temp,k)
            if kthnode==None:
                if prevnode:
                    prevnode.next = temp
                break
            nextnode = kthnode.next
            kthnode.next = None
            self.reverse(temp)
            if temp==head:
                head = kthnode
            else:
                prevnode.next = kthnode
            prevnode = temp
            temp = nextnode
        return head
