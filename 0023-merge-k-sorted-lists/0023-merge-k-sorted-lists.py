# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergesort(self,head1,head2):
        dummynode = ListNode()
        temp = dummynode
        left = head1
        right = head2
        while(left!=None and right!=None):
            if left.val<=right.val:
                temp.next  = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left if left else right
        return dummynode.next
        
    def mergeKLists(self, lists):
        n = len(lists)
        dummynode = ListNode()
        ans = dummynode
        if n==1:
            return lists[0]
        i = 1
        while(len(lists)>1 and i<n):
            if ans.next==None:
                ans.next = self.mergesort(lists[i],lists[i-1])
            else:
                ans.next = self.mergesort(ans.next,lists[i])
            i+=1
        return ans.next


        


        