# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_lists(self,head1,head2):
        dummy = ListNode(-1)
        temp = dummy
        temp1 = head1
        temp2 = head2
        while temp1 and temp2:
            if temp1.val<temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        while temp1:
            temp.next = temp1
            temp1 = temp1.next
            temp = temp.next
        while temp2:
            temp.next = temp2
            temp2 = temp2.next
            temp = temp.next
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        n = len(lists)
        merged = lists[0]
        for i in range(1,n):
            merged = self.merge_lists(merged,lists[i])
        return merged