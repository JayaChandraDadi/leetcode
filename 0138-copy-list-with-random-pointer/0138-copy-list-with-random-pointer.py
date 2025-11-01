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
        if not head:
            return 
        temp = head
        while(temp!=None):
            newnode = Node(temp.val)
            newnode.next = temp.next
            temp.next = newnode
            temp = temp.next.next
        temp = head
        while(temp!=None):
            if temp.random:
                temp.next.random = temp.random.next
            else:
                temp.next.random = None
            temp = temp.next.next
        dummynode = Node(-1)
        temp = head
        dummynode.next = temp.next
        while(temp!=None):
            front = temp.next
            temp.next = temp.next.next
            if front.next:
                front.next = front.next.next
            else:
                front.next = None
            temp = temp.next
        return dummynode.next
