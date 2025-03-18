"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
       if head==None:
        return
       temp = head
       while(temp!=None):
        newnode = Node(temp.val)
        newnode.next = temp.next
        temp.next = newnode
        temp = temp.next.next
       temp = head
       while(temp!=None):
        copynode = temp.next
        if temp.random==None:
            copynode.random = None
        else:
            copynode.random = temp.random.next
        temp = temp.next.next
       dummynode = Node(-1)
       res = dummynode
       temp = head
       while(temp!=None):
        res.next = temp.next
        temp.next = temp.next.next
        res = res.next
        temp = temp.next
       return dummynode.next



        