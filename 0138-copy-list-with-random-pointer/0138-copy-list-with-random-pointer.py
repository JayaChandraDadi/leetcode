"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        temp = head
        while(temp!=None):
            newnode = Node(temp.val)
            newnode.next = temp.next
            temp.next = newnode
            temp = temp.next.next
        newhead = head.next
        temp = head
        while(temp!=None):
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        temp = head
        while(temp!=None):
            temp1 = temp.next
            temp.next = temp.next.next
            if temp1.next:
                temp1.next = temp1.next.next
            temp = temp.next
        return newhead
