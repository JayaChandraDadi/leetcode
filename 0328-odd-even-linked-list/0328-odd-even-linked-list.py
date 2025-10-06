# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        oddhead = ListNode()
        evenhead = ListNode()
        odd = oddhead
        even = evenhead
        temp = head
        index = 1
        while(temp!=None):
            if index%2!=0:
                odd.next = temp
                odd = odd.next
            else:
                even.next = temp
                even = even.next
            temp = temp.next
            index+=1
        even.next = None
        odd.next = evenhead.next
        return oddhead.next


            

        
        